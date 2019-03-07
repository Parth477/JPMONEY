from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html', c)


# Create your views here.
 