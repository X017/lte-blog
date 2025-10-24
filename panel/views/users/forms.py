# forms.py
from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, HTML, Div
from crispy_forms.bootstrap import PrependedText

User = get_user_model()

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''  # Current URL
        
        # Add form layout
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('first_name', css_class='form-control'),
            Field('last_name', css_class='form-control'),
            Field('password', css_class='form-control'),
            
            Div(
                Submit('submit', '{% if object %}ذخیره تغییرات{% else %}ایجاد کاربر{% endif %}', 
                       css_class='btn btn-primary'),
                HTML('<a href="{% url \'users:list\' %}" class="btn btn-default">بازگشت</a>'),
                css_class='form-group text-left'
            )
        )
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
