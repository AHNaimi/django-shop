from django.shortcuts import render
from django.views import View


class HomeView(View):
    """ a class that show home page dynamically """
    def get(self, request):
        return render(request, 'home/homepage.html')
