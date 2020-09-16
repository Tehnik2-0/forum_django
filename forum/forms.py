from django import forms
from .models import Article, Comment
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import Textarea


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
                'title',
                'body'
                )

    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args,
                         **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = (
                'username',
                'password'
                )

    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args,
                         **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
                'username',
                'password'
                )

    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args,
                         **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
   
    def save(self,
             commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args,
                         **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['body'].widget = Textarea(attrs={'rows': 5})