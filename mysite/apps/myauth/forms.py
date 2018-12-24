# -*- coding: utf-8 -*-
from django import forms
from .models import Myuser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Myuser
        fields = ['avatar','signature'] #只显示model中指定的字段

