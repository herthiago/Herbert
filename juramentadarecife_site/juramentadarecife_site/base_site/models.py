# -*- coding:utf-8 -*-
from django.db import models
from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    mensagem = forms.CharField(required=True, widget=forms.Textarea())


class OrcamentoForm(forms.Form):
    nome = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    descricao = forms.CharField(required=True, widget=forms.Textarea())
