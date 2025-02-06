from django.urls import re_path
from . import views

urlpatterns = [
    re_path("studentForm/", views.student_input_view),
    re_path("feedbackForm/", views.feedback_view),
    re_path("signupForm/", views.signup_form_view),

]
