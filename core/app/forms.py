from django import forms
from .models import Object

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Поиск')
class ObjectCreateForm(forms.ModelForm):

    class Meta:
        model = Object
        fields = (
            'title',
            'category',
            'logo',
            'description',
            'date',
            'views',
            'type'
        )
class ObjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['title', 'category', 'logo', 'description', 'date', 'views', 'type']


