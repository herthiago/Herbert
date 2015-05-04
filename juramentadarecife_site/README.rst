=========================
juramentadarecife project
=========================

Projeto do site www.juramentadarecife.com.br


Este site foi construído com o framework web Django (versão 1.6.5) e Python (versão 3.4). A configuração para o desenvolvimento do projeto é bastante simples.

Instalação do Python
====================

Se você estiver em um sistema Linux ou Mac OS X, o Python provavelmente já está instalado. Se não estiver instalado ou
se não estiver usando um desses sistemas, uma busca rápida na internet pode ajudar na instalação do Python.
Ou, se preferir siga as instruções neste link: http://www.pythonize.org/blog/iniciando-programacao-python/

Instalação de virtualenv
========================

Recomendamos utilizar o virtualenv para separar as dependências deste projeto do ambiente python do seu sistema.
Se você estiver em um sistema Linux ou Mac OS X, você pode utilizar o virtualenvwrapper para ajudar a gerenciar
diversos virtualenvs criados para diferentes projetos.

Virtualenv
----------

Após a instalação do virtualenv, crie um ambiente::

    $ virtualenv juramentada

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.

Virtualenv com virtualenvwrapper
------------------------------------

No Linux e Mac OSX, você pode instalar o virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
que gerencia seus ambientes virtuais e adiciona o path do projeto ao `site-directory`::

    $ mkdir juramentada
    $ mkvirtualenv -a juramentada juramentada-dev
    $ cd juramentada && add2virtualenv `pwd`

Usando virtualenvwrapper no Windows
----------------------------------------

Existe uma versão especial do virtualenvwrapper para Windows (https://pypi.python.org/pypi/virtualenvwrapper-win).::

    > mkdir juramentada
    > mkvirtualenv juramentada-dev
    > add2virtualenv juramentada


Instalando os pacotes necessários
=================================

Dependendo de onde vocês está instalando as dependências, basta ir até o diretório do projeto aonde está o arquivo
requirements.txt e executar o seguinte:

Em desenvolvimento::

    $ pip install -r requirements/local.txt

Para produção::

    $ pip install -r requirements.txt

Follows Best Practices
======================

.. image:: http://twoscoops.smugmug.com/Two-Scoops-Press-Media-Kit/i-C8s5jkn/0/O/favicon-152.png
   :name: Two Scoops Logo
   :align: center
   :alt: Two Scoops of Django
   :target: http://twoscoopspress.org/products/two-scoops-of-django-1-6

This project follows best practices as espoused in `Two Scoops of Django: Best Practices for Django 1.6`_.

.. _`Two Scoops of Django: Best Practices for Django 1.6`: http://twoscoopspress.org/products/two-scoops-of-django-1-6
