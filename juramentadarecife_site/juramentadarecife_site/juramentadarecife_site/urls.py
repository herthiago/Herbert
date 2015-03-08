from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', TemplateView.as_view(template_name='index.html')),

    # Examples:
    # url(r'^$', 'juramentadarecife_site.views.home', name='home'),
    # url(r'^juramentadarecife_site/', include('juramentadarecife_site.foo.urls')),
    url(r'^$', 'base_site.views.index', name='index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^saiba-mais/', 'base_site.views.saiba_mais', name='saiba_mais'),
    url(r'^o-que/', 'base_site.views.traducao_juramentada', name='traducao_juramentada'),
    url(r'^como-solicitar/', 'base_site.views.como_solicitar', name='como_solicitar'),
    url(r'^quanto-custa/', 'base_site.views.quanto_custa', name='quanto_custa'),
    url(r'^faq/', 'base_site.views.faq', name='faq'),
    url(r'^contato/', 'base_site.views.contato', name='contato'),
    url(r'^consulados/', 'base_site.views.consulados', name='consulados'),
)

urlpatterns += patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
