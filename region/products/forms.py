from django.forms import ModelForm
from .models import Review

class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']

# users/forms.py
from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
