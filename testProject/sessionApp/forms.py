from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(max_length=44)


class ItemAddForm(forms.Form):
    itemname = forms.CharField(max_length=100)
    quantity = forms.IntegerField(max_value=30)


class NameForm(forms.Form):
    name = forms.CharField()


class AgeForm(forms.Form):
    age = forms.IntegerField()


class GFForm(forms.Form):
    gf = forms.CharField()
