from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django import forms
from .models import Account, CatItem
from .forms import AboutForm, AuthForm, RegForm


def check(request):
    request.session['is_authorised'] = True


def catalog(request):
    filt = request.POST['filter']
    items = list(CatItem.objects.filter(CatItem.category == filt))
    return render(request, 'catalog.html', {'items': items})


def fav(request):
    acc = None
    if request.session.get('is_authorised'):
        acc = request.session.get('account_name')
        return render(request, 'favs.html', {'account_name': acc})
    else:
        return HttpResponseRedirect('auth.html')


def session_save(request, login):
    request.session['account_name'] = login


class MainView(generic.TemplateView):
    template_name = 'main.html'


class AuthView(generic.FormView):
    template_name = 'auth.html'
    form_class = AuthForm
    success_url = 'favs.html'

    def form_valid(self, form):
        session_save(None, AuthForm.login)
        return super().form_valid(form)


class RegView(generic.FormView):
    template_name = 'reg.html'
