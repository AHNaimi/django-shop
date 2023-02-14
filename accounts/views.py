from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm
from .models import UserModel
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import views as authen_view
# from django.urls import reverse_lazy


class UserRegisterView(View):
    form = UserForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:homepage')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form1 = self.form
        return render(request, 'accounts/register.html', {"form": form1})

    def post(self, request):
        form1 = self.form(request.POST)
        if form1.is_valid():
            valid_form = form1.cleaned_data
            user = UserModel.objects.create_user(valid_form['email'], valid_form['first_name'],
                                                 valid_form['last_name'], valid_form['phone'], valid_form['address'],
                                                 valid_form['password'])
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'you registered successfully')
            return redirect('home:homepage')
        return render(request, 'accounts/register.html', {"form": form1})


class UserLogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        messages.info(request, "you log out successfully")
        return redirect("home:homepage")
