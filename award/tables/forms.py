from django import forms
from .models import Employee
from .models import Post
from .models import Awards
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        fields = ['full_name', 'phone', 'email']


class SearchForm(forms.Form):
    name = forms.CharField(label='Имя сотрудника')
    post = forms.ModelChoiceField(queryset=Post.objects.all(), empty_label='Выберите должность', required=False)
    awards = forms.ModelChoiceField(queryset=Awards.objects.all(), empty_label='Выберите награду', required=False)



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'fk_post', 'fk_awards', 'hire', 'kgtu_hire']

