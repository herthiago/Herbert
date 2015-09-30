# -*- coding:utf-8 -*-

import os
from django.shortcuts import render_to_response
from django.core.mail import send_mail, EmailMessage
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from base_site.models import ContatoForm, OrcamentoForm
from django.core.urlresolvers import reverse


def index(request):
    dict_template = {}
    return render_to_response("index.html", dict_template, context_instance=RequestContext(request))


def saiba_mais(request):
    dict_template = {}
    return render_to_response("saiba_mais.html", dict_template, context_instance=RequestContext(request))


def traducao_juramentada(request):
    dict_template = {}
    return render_to_response("traducao_juramentada.html", dict_template, context_instance=RequestContext(request))


# def como_solicitar(request):
#     dict_template = {}
#     return render_to_response("como_solicitar.html", dict_template)


def quanto_custa(request):
    dict_template = {}
    return render_to_response("quanto_custa.html", dict_template, context_instance=RequestContext(request))


def faq(request):
    dict_template = {}
    return render_to_response("faq.html", dict_template, context_instance=RequestContext(request))


def contato(request):
    dict_template = {}
    return render_to_response("contato.html", dict_template, context_instance=RequestContext(request))


def consulados(request):
    dict_template = {}
    return render_to_response("consulados.html", dict_template, context_instance=RequestContext(request))


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            send_mail(
                "E-mail para Andrea Bayle - Contato: %s" % email,
                "Mensagem:\n%s" % mensagem,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_TO_EMAIL],
                fail_silently=False
            )

            return HttpResponseRedirect(reverse("contato_ok"))

    else:
        form = ContatoForm()

    dict_template = {
        'form': form,
    }
    return render_to_response("contato.html", dict_template, context_instance=RequestContext(request))


def contato_ok(request):
    dict_template = {}
    return render_to_response("contato_ok.html", dict_template, context_instance=RequestContext(request))


def como_solicitar(request):
    if request.method == 'POST':
        form = OrcamentoForm(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email_str = form.cleaned_data['email']
            mensagem = form.cleaned_data['descricao']

            # obtém o documento do form
            docfile = request.FILES['documento']
            docpath = settings.SITE_ROOT + "/documentos/"

            # salva o documento no diretório especificado
            doc_fullpath = save_document(docfile, docpath)

            email = EmailMessage("Email: %s" % email_str,
                                 "Mensagem:\n%s" % mensagem,
                                 settings.DEFAULT_FROM_EMAIL,
                                 [settings.DEFAULT_TO_EMAIL])

            email.attach_file(doc_fullpath)
            email.send(fail_silently=False)

            return HttpResponseRedirect(reverse("contato_ok"))

    else:
        form = OrcamentoForm()

    dict_template = {
        'form': form,
    }

    return render_to_response("como_solicitar.html", dict_template, context_instance=RequestContext(request))


def save_document(docfile, docpath):
    from unicodedata import normalize
    nome = normalize('NFKD', os.path.basename(docfile.name)).encode('ASCII', 'ignore')
    doc_fullpath = docpath + str(nome.decode())
    with open(doc_fullpath, 'wb+') as documento:
        for chunk in docfile.chunks():
            documento.write(chunk)

    return doc_fullpath
