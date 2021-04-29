from django import forms
from django.db.models import fields
from django.forms.forms import Form
from django.forms.models import ModelForm
from django.db import models
from .models import *


class Contactform(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
