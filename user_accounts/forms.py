from django import forms
from .models import User


class UserCreateForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'role',
            'is_active',
        ]