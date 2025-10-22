from django.contrib.auth import get_user_model
from django.forms import ModelForm

User = get_user_model()  

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password']
