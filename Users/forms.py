from django import forms
from django.contrib.auth.models import User
from Users.models import UserProfile, Task
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
class UserForm(UserCreationForm):
    email=forms.EmailField()
    class Meta():
        model = User
        fields=('username','first_name','last_name','email','password1','password2')
        labels = {'password1':'Password',
                  'password2':'Confirm Password'
                 }

class StudentProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    student = 'student'
    user_types = [(student,'student'),
                ]
    user_type = forms.ChoiceField(required=True,choices=user_types)
    class Meta():
        model=UserProfile
        fields=('bio','profile_pic','user_type','standard')

class TeacherProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    teacher = 'teacher'
    user_types = [(teacher,'teacher')]
    user_type = forms.ChoiceField(required=True,choices=user_types)
    class Meta():
        model=UserProfile
        fields=('bio','profile_pic','user_type')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('completed','ppt')
