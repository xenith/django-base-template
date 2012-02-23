from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import RequestContext


def home(request):
    return render_to_response('base/home.html',
        context_instance=RequestContext(request))
