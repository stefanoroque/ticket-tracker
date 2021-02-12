from django import forms
from .models import User

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


class NewSigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), label='')
    

class NewProjectForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}), label='')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Project Description', "rows":5, "cols":20}), label='')
    
    all_users = User.objects.all()
    user_options = []
    # Create option list of users that can be assigned to a project
    for u in all_users:
        user_tuple = (u.id, u.first_name + " " + u.last_name)
        user_options.append(user_tuple)

    # TODO: Change this to a multiple select dropdown box
    assigned_users = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Assigned Users',
                                          choices=user_options)
    
    