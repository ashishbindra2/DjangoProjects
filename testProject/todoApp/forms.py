from django import forms


class TodoInputForm(forms.Form):
    task = forms.CharField(min_length=1,label='', widget=forms.TextInput(attrs={"class": "form-control"}))
    task.widget.attrs['required'] = 'required'
    task.widget.attrs['placeholder'] = 'Add Your TODO'
