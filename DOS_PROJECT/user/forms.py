from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserLogin(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist or incorrect Password')
                
# class UserSignUp(forms.Form):
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)


#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name' ,'password1', 'password2']

#     def save(self, commit=True):
#         user = super(UserSignUp, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

class UserSignUp(UserCreationForm):
    email = forms.EmailField(required=True)
    is_student = forms.BooleanField(required=False)
    is_teacher = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_student', 'is_teacher']

    def save(self, commit=True):
        user = super(UserSignUp, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_vendor = True
        user.is_teacher = False
        if commit:
            user.save()
        return user
