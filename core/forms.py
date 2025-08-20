from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Contact 



class CustomUserCreationForm(UserCreationForm):
    
    full_name = forms.CharField(
                           required= True, 
                           widget= forms.TextInput( attrs = {'placeholder': 'Full Name'}))
    
    email = forms.EmailField(
                             required= True, 
                             widget = forms.EmailInput(attrs={'placeholder' : 'Email'}))
    
    class Meta:
        model = User
        fields = ('full_name', 'email','password1', 'password2' )


    def save(self, commit = True):
        user = super().save(commit= False)
        self.username = self.cleaned_data['email'] 
        user.full_name = self.cleaned_data['full_name']
        if commit:
            user.save()
        return user


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'company', 'status', 'notes']  # Fields you want to include in the form

        widgets = {
            'status': forms.Select(choices=Contact.STATUS_CHOICES),
            'notes': forms.Textarea(attrs={'placeholder': 'Add some notes...'}),
        }
    
