from django import forms
from .models import Comment
from django.contrib.auth.models import User
from .models import Profile

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'border p-2 rounded w-full mb-2'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write a comment...', 'class': 'border p-2 rounded w-full mb-2'}),
        }



from .models import Profile



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'cover_photo','birth_date','location','skills']
