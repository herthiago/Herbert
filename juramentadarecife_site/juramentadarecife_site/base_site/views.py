from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from base_site.models import ContatoForm
from smtplib import SMTPException


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


def quanto_custa(request):
    dict_template = {}
    return render_to_response("quanto_custa.html", dict_template)


def faq(request):
    dict_template = {}
    return render_to_response("faq.html", dict_template)


def contato(request):
    dict_template = {}
    return render_to_response("contato.html", dict_template)


def consulados(request):
    dict_template = {}
    return render_to_response("consulados.html", dict_template)


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            send_mail(
                "E-mail: %s" % email,
                "Mensagem:\n%s" % mensagem,
                "andersonberg@gmail.com",
                ["andersonberg@gmail.com"],
                #settings.DEFAULT_FROM_EMAIL,
                #[settings.DEFAULT_TO_EMAIL],
                fail_silently=False
            )

            return render_to_response("contato.html")

    else:
        form = ContatoForm()

    dict_template = {
        'form': form,
    }
    return render_to_response("contato.html", dict_template, context_instance=RequestContext(request))
