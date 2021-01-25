from django import forms

ROLE_CHOICES =( 
    ("Developer", "Developer"), 
    ("Project Manager", "Project Manager"), 
    ("Submitter", "Submitter"), 
    ("Administrator", "Administrator"), 
) 

class NewRegisterForm(forms.Form):
    username = forms.CharField(label="Username", 
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    first_name = forms.CharField(label="First Name", 
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}))
    last_name = forms.CharField(label="Last Name", 
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}))
    email = forms.EmailField(label="Email Address", 
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    role = forms.ChoiceField(choices = ROLE_CHOICES, 
                            widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    confirmation = forms.CharField(label="Confirm Password", 
                            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter password'}))