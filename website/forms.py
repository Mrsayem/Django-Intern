from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record



class SignUpForm(UserCreationForm):
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Name'}))
    email =forms.CharField(label="", max_length=100,required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your phone email'}))
    image = forms.ImageField(label="", required=False, widget=forms.FileInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ( 'username','name', 'email','image', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class AddRecordForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Enter your name ", "class":"form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Enter your email ", "class":"form-control"}), label="")
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))
    title = forms.CharField(max_length=100, required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Enter vlog title ", "class":"form-control"}), label="")
    description = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"Enter vlog description ", "class":"form-control"}), label="")
    vlog_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Record
        fields = ['name', 'email', 'image', 'title', 'description', 'vlog_image']