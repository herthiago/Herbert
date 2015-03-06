from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    dict_template = {}
    return render_to_response("index.html", dict_template)


def saiba_mais(request):
    dict_template = {}
    return render_to_response("saiba_mais.html", dict_template)


def traducao_juramentada(request):
    dict_template = {}
    return render_to_response("traducao_juramentada.html", dict_template)


def como_solicitar(request):
    dict_template = {}
    return render_to_response("como_solicitar.html", dict_template)
