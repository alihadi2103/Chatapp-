from django.forms import forms, Form
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator




from django import forms
from django.forms import Form

class SignupForm(Form):
    username = forms.CharField(
        max_length=20,
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )
    def is_valid(self) -> bool:
        
        cleaned_password=self.clean(self.password)
        cleaned_confirmpassword=self.clean(self.confirm_password)
        
        if  super().is_valid() and self.cleaned_password==cleaned_confirmpassword :
            return True
        else:
            return False


class OtpForm(Form):

      integer_field = forms.CharField(
        label="Integer Field",
        validators=[
            MinLengthValidator(8),
            MaxLengthValidator(8),
            RegexValidator(regex='^\d{8}$', message='This field must be exactly 8 digits.')
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Enter the code has been sent to your email'})
            )