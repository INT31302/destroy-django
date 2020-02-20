from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confimation', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('user_id', 'password1', 'password2',
                  'email', 'date_of_birth', 'phone')
        labels = {
            'user_id': '아이디',
            'email': '이메일',
            'date_of_birth': '생년월일',
            'password1': '비밀번호',
            'password2': '비밀번호 확인',
            'phone': '전화번호'
        }
        widgets = {
            'user_id': forms.TextInput(attrs={
                'class': 'form-control', 'style': 'width:500px;', 'name': 'user_id'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control', 'style': 'width:500px;', 'name': 'password1'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control', 'style': 'width:500px;', 'name': 'password2'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'style': 'width:500px;', 'name': 'eamil'
            }),
            'date_of_birth': forms.TextInput(attrs={
                'class': 'form-control', 'style': 'width:500px;', 'name': 'date_of_birth'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'style': 'width:500px;', 'name': 'password'
            }),

        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('user_id', 'email', 'password', 'date_of_birth', 'phone',
                  'is_active', 'is_admin')

        def clean_password(self):
            return self.inital["password"]


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'password']
        labels = {
            'user_id': '아이디',
            'password': '비밀번호'
        }
        widgets = {
            'user_id': forms.TextInput(attrs={
                'class': 'form-control', 'style': 'width:500px;', 'name': 'user_id'
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control', 'style': 'width:500px;', 'name': 'password', 'type': 'password'
            })
        }
