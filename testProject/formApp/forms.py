from django import forms


class StudentForm(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()


# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)

# Explicitly by the Programmer by using Clean Methods:
# The syntax of clean method: clean_fieldname(self)

# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)
#
#     def clean_name(self):
#         inputname = self.cleaned_data['name']
#         if len(inputname) < 4:
#             raise forms.ValidationError('The Minimum no of characters in the name field should be 4')
#         return inputname + 'durga'
#
#     def clean_rollno(self):
#         inputrollno = self.cleaned_data['rollno']
#         print('Validating rollno field')
#         return inputrollno
#
#     def clean_email(self):
#         inputemail = self.cleaned_data['email']
#         print('Validating email field')
#         return inputemail
#
#     def clean_feedback(self):
#         inputfeedback = self.cleaned_data['feedback']
#         print('Validating feedback field')
#         return inputfeedback


# 2) Django's Inbuilt Core Validators:
# from django.core import validators
# class FeedBackForm(forms.Form):
#     name=forms.CharField()
#     rollno=forms.IntegerField()
#     email=forms.EmailField()
#     feedback=forms.CharField(widget=forms.Textarea,validators= [validators.MaxLengthValidator(40)])


# How to implement Custom Validators by using the same Validator Parameter:
# def starts_with_d(value):
#     if value[0].lower() != 'd':
#         raise forms.ValidationError('Name should be starts with d | D')
#
#
# class FeedBackForm(forms.Form):
#     name = forms.CharField(validators=[starts_with_d])
#     rollno = forms.IntegerField()

# Validation of Total Form directly by using a Single Clean Method:

# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)
#
#     def clean(self):
#         print('Total Form Validation...')
#         total_cleaned_data = super().clean()
#
#         inputname = total_cleaned_data['name']
#         inputrollno = total_cleaned_data['rollno']
#
#         if inputname[0].lower() != 'd':
#             raise forms.ValidationError('Name parameter should starts with d')
#
#         if inputrollno <= 0:
#             raise forms.ValidationError('Rollno should be > 0')

# How to prevent BOT Requests: ☕
# Note: Other ways to prevent BOT requests
# 1) By using Captchas
# 2) By using image recognizers (like choose 4 images where car present)
# class FeedBackForm(forms.Form):
#     name=forms.CharField()
#     password=forms.CharField(widget=forms.PasswordInput)
#     rpassword=forms.CharField(label='Re Enter Password', widget=forms.PasswordInput)
#     rollno=forms.IntegerField()
#     email=forms.EmailField()
#     feedback=forms.CharField(widget=forms.Textarea)
#     bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
#     def clean(self):
#         print('validating passwords match...')
#         total_cleaned_data=super().clean()
#         fpwd=total_cleaned_data['password']
#         spwd=total_cleaned_data['rpassword']
#         if fpwd != spwd:
#             raise forms.ValidationError('Both passwords must be matched')
#
#         bot_handler_value=total_cleaned_data['bot_handler']
#         if len(bot_handler_value)>0:
#             raise forms.ValidationError('Request from BOT...cannot be submitted!!!')

# Notes with BOT Field: 1)
class FeedBackForm(forms.Form):
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
    name = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Re Enter Password', widget=forms.PasswordInput)
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    def clean(self):
        total_cleaned_data=super().clean()
        bot_handler_value=total_cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Request from BOT...cannot be submitted!!!')
class SignupForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Reenter Password', widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean(self):
        total_cleaned_data = super().clean()
        pwd = total_cleaned_data['password']
        rpwd = total_cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError('Both Passwords must be same')
