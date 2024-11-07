from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

# class LoginForm(forms.Form):
#     template_name = "botpanel/form_snippet.html"
#     text = forms.CharField(label="Текст кнопки", max_length=50)
#     result = forms.CharField(max_length=9900, widget=forms.Textarea, label="Сообщение")
    
#     def __init__(self, *args, **kwargs):
#         super(LoginForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
            
            
class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий email.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'