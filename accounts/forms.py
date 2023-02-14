from django import forms
from accounts.models import UserModel
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    """a form for users sign in process"""
    password2 = forms.CharField(required=True, min_length=8, max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'phone', 'address', 'password', 'password2')
        widgets = {
            'password': forms.PasswordInput
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        user_email = UserModel.objects.filter(email=email).exists()
        if user_email:
            raise ValidationError('this email is already in use')
        return email

    def clean(self):
        cd = super().clean()
        password1 = cd.get("password")
        password2 = cd.get("password2")
        if password1 and password2 and password2 != password1:
            raise ValidationError('passwords are not match')
