
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import LoginForm, CalcForm


class Login(View):
    template = 'login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template, locals())

    def post(self, request, *args, **kwargs):

        form = LoginForm(request.POST)
        if form.is_valid():
            print(str(form.cleaned_data['username'])+' '+str(form.cleaned_data['password']) )
            if form.cleaned_data['username'] == 'user' and form.cleaned_data['password'] == '12345':
                request.session['user'] = form.cleaned_data['username']

                return redirect('pintura')
            else:
                error = 'Usuario o contraseñas incorrectos'
        else:
            print(form.errors)
        return render(request, self.template, locals())

class Calculo(View):
    template = 'calculo.html'

    def get(self, request, *args, **kwargs):
        form = CalcForm()
        return render(request, self.template, locals())

    def post(self, request, *args, **kwargs):
        form = CalcForm(request.POST)

class Logout(View):
    template = 'logout.html'

    def get(self, request, *args, **kwargs):
        request.session['user']= False

        return render(request, self.template, locals())