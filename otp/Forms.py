from django.forms import forms, Form 

from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.contrib.auth.models import User




from django import forms
from django.forms import Form

class SignupForm(forms.ModelForm):
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
    def is_valid(self):
    # Call the parent class's is_valid to populate cleaned_data
    
    
        is_valid = super().is_valid()
    
        if is_valid:  # Check if the form is valid first
                cleaned_password = self.cleaned_data.get('password')
                cleaned_confirm_password = self.cleaned_data.get('confirm_password')
        
                if cleaned_password and cleaned_confirm_password:
                        if cleaned_password == cleaned_confirm_password:
                            return True
                        else:
                            self.add_error('confirm_password', "Passwords do not match.")
                            return False
                else:
                    self.add_error('password',"This field is required.")
                    return False
        return False  # Return False if the form is not valid

    
    
    
    
    class Meta:
        model=User
        fields=["username", "password", "email"]
        
    
    
    


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