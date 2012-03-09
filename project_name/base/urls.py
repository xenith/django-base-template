from django.conf.urls.defaults import url, include, patterns


urlpatterns = patterns('{{ project_name}}.base.views',
    url(r'^$', 'home', name='home'),
)
