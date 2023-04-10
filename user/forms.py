from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms 

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Nike Nmame...'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'First Email...'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Last Name...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type':'email','placeholder':'Email adress...'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Password...','id':'pass'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Confirm Password...','id':'pass2'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    password = forms.CharField(widget=forms.TextInput(attrs={}))

    class Meta:
        model = User
        fields = ('username','password')
        
        
class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={}))
    # image = forms.ImageField(widget=forms.FileInput(attrs={'type':'text','placeholder':'Email...'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={}))
    
    

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','image')