from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache

from .forms import UserCreateForm


@never_cache
def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(
            request,
            'login.html',
            {
                'error': 'Invalid email or password.'
            }
        )

    return render(request, 'login.html')


@never_cache
def logout_view(request):
    logout(request)
    return redirect('login')


def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect('login')

            if request.user.role not in allowed_roles:
                return redirect('home')

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


@login_required
def create_user(request):

    if request.user.role != 'admin':
        return redirect('home')

    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('home')

    else:
        form = UserCreateForm()

    return render(
        request,
        'users/create_user.html',
        {'form': form}
    )