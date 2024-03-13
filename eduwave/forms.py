from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from app.models import UserProfile  # Ensure this import is correct

def validate_email_unique(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError("Email already exists.")

class CustomRegistrationForm(forms.Form):
    ROLE_CHOICES = (
        ('learner', 'Learner'),
        ('teacher', 'Teacher'),
    )
    
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True, validators=[validate_email_unique])
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    # password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)


    def save(self):
        # Ensure the user instance is created with the specified username, email, and password
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        # Create and save the UserProfile instance associated with the user
        UserProfile.objects.create(user=user, role=self.cleaned_data['role'])
        return user