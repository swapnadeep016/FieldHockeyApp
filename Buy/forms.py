from django import forms
from django.core import validators

class SignupForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100)
	email = forms.EmailField(label = 'Email',max_length=100)
	password = forms.CharField(label='Password', max_length=100)
	cpassword = forms.CharField(label='Confirm Password', max_length=100)
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, 
								validators=[validators.MaxLengthValidator(0)])

	def clean(self):
		allData = super().clean()
		p = allData['password']
		c = allData['cpassword']
		if p!=c:
			raise forms.ValidationError("Password and Confirm Password does not match!!")

	def raiseError(self):
		raise forms.ValidationError("Something went wrong!! Try again.")
	# def clean_botcatcher(self):
	# 	inp = self.cleaned_data['botcatcher']
	# 	if len(inp) > 0 :
	# 		raise forms.ValidationError("Gotcha Bot!!")

class LoginForm(forms.Form):
	email = forms.CharField(label='Email Id', max_length=100)
	password = forms.CharField(label='Password', max_length=100)