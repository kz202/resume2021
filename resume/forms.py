from django import forms

class EmailPostForm(forms.Form):
        name = forms.CharField(max_length=50,label='Name  ')
        email = forms.EmailField(label='Email  ')
        notice = forms.CharField(required=True, widget=forms.Textarea)