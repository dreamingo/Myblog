#coding=utf-8
from django import forms

class BlogForm(forms.Form):
	caption = forms.CharField(max_length=50, widget = forms.TextInput(
		attrs = {'placeholder': '标题'}))
	content = forms.CharField(widget=forms.Textarea)
	tag_name = forms.CharField(max_length=20, required=False)
	category = forms.CharField(max_length=100)


class CommentForm(forms.Form):
	name = forms.CharField(max_length=100, widget=forms.TextInput( attrs = {'placeholder': 'Enter your name'}))
	email = forms.EmailField( widget=forms.TextInput( attrs = {'placeholder': 'Enter your Email-address'}))
	content = forms.CharField(widget=forms.Textarea( attrs = {'class':'input-xlarge comment',
		'placeholder': 'Please Enter your comment'}))

class LoginForm(forms.Form):
	name = forms.CharField(max_length=100, widget=forms.TextInput( attrs = {'placeholder': 'Name'}))
	password = forms.CharField(max_length=100, widget=forms.PasswordInput( attrs = {'placeholder':'Password',
		}))

