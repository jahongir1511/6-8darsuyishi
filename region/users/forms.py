from django import forms
from users.models import CustomUser


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)  # Don't commit yet to avoid saving twice
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user