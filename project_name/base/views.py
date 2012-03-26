""" Views for the base application """

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    """ Default view for the root """
    return render_to_response('base/home.html',
        context_instance=RequestContext(request))
