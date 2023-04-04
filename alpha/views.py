from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.views import generic
from django.forms import ValidationError
from .models import CatItem, FavItems
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .forms import AboutForm, AuthForm, RegForm
from django.utils.datastructures import MultiValueDictKeyError


def check(request):
    request.session['is_authorised'] = True


def catalog(request):
    filt = None
    try:
        filt = request.GET['filter']
    except MultiValueDictKeyError:
        filt = 'all'

    if filt == 'all':
        items = list(CatItem.objects.all())
    else:
        items = list()
        for cat in CatItem.objects.all():
            if cat.category == filt:
                items.append(cat)
    return render(request, 'catalog.html', {'items': items, 'filt': filt})


def favs(request):
    if request.session.get('is_authorised'):
        ac = User.objects.all().filter(login__exact=request.session.get('account_name'))
        if not ac:
            raise "Не удалось авторизоваться"
        acpk = ac.pk  # получаю pk аккаунта
        items = FavItems(acpk=acpk).itpk.objects.all()  # по pk получаю объекты добавленных предметов
        return render(request, 'favs.html', {'account_name': ac.login, 'items': items})
    else:
        return HttpResponseRedirect('../auth')


class MainView(generic.TemplateView):
    template_name = 'main.html'


class AuthView(LoginView):
    template_name = 'auth.html'
    redirect_authenticated_user = True
    authentication_form = AuthForm

    def form_invalid(self, form):
        errors = form.errors.as_data()
        error = None
        if str(errors['__all__']).find("ValidationError"):
            error = "Неверная электронная почта или пароль."
        else:
            error = str(errors['__all__'][0])[2:len(str(errors['__all__'][0]))-2]
        return render(self.request, self.template_name, {"error": error, "form": form})


class RegView(generic.CreateView):
    template_name = 'reg.html'
    redirect_authenticated_user = True
    model = User
    fields = ["username", "password"]

    def form_invalid(self, form):
        errors = form.errors.as_data()
        error = None
        if str(errors['__all__']).find("ValidationError"):
            error = "Неверная электронная почта или пароль."
        else:
            error = str(errors['__all__'][0])[2:len(str(errors['__all__'][0])) - 2]
        return render(self.request, self.template_name, {"error": error, "form": form})


class AboutView(generic.FormView):
    template_name = 'about.html'
    form_class = AboutForm
    success_url = ''
