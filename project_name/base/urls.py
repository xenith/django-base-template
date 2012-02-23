from django.conf.urls.defaults import *


urlpatterns = patterns('{{ project_name}}.base.views',
    url(r'^$', 'home', name='home'),
)
