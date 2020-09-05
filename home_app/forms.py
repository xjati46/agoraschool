from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from account_app.models import CustomUser


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nama User'
        self.fields['password1'].label = 'Password'
        self.fields['email'].label = 'Alamat E-Mail'
        self.fields['password1'].help_text = 'Minimal 8 karakter'
        self.fields['password2'].label = 'Konfirmasi Password'
        self.fields['password2'].help_text = 'Ketik ulang Password'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = [
            'username', 'password', 'email',
            'is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions',
            'date_joined', 'last_login',
            ]
