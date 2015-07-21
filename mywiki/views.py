from mywiki.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from .forms import *
from .rforms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404
import json

# Create your views here.

def homepage(request):
   if request.method == 'POST':
	form = WikiModelForm(request.POST)
        if form.is_valid():
	    form.save()
            return render_to_response(
    'home.html',
    { 'user': request.user, 'wiki_list': Wiki.objects.all() }
    )
   else:
	form = WikiModelForm()
   return render_to_response('homepage.html', {
      'form': form}, context_instance=
      RequestContext(request))

def showsearch(request):
    if(request.method == "POST") :
        ss = request.POST['search']
        return render_to_response('searchview.html', {'wiki_list': Wiki.objects.all().filter(title=ss) }, context_instance = RequestContext(request))

def update(request, id):
   a = Wiki.objects.get(pk=id)
   f = WikiModelForm(request.POST, instance=a)
   if f.is_valid():
       f.save()
       return render_to_response('home.html', { 'user': request.user, 'wiki_list': Wiki.objects.all() })
   else:
       f = WikiModelForm(initial={'title':a.title, 'body':a.body, 'posted':a.posted})
   return render_to_response('homepage.html', {
      'form': f}, context_instance=
      RequestContext(request))

def delete(request, id):
   dat = Wiki.objects.get(pk = id)
   dat.delete()
   return render_to_response(
    'home.html',
    { 'user': request.user, 'wiki_list': Wiki.objects.all() }
    )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user, 'wiki_list': Wiki.objects.all() }
    )
def firstpage(request):
    return render_to_response(
    'firstpage.html',
    { 'user': request.user, 'wiki_list': Wiki.objects.all() }
    )
def get_search(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        search = Wiki.objects.filter(title__icontains = q )
        results = []
        for ss in search:
            search_json = {}
            search_json['label'] = ss.title
            search_json['value'] = ss.title
            results.append(search_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

