from django.shortcuts import render, redirect
from django.views import View
from home.models import CategoryModel


class HomeView(View):
    """ a class that show home page dynamically """

    def get(self, request):
        return render(request, 'home/homepage.html')


class CategoryView(View):
    """ a class for showing products of selected category"""

    def get(self, request, cat_slug_url):
        cat = CategoryModel.objects.get(cat_slug=cat_slug_url)
        products = cat.pro_model.all()
        return render(request, 'home/categorypage.html', {"products": products, "category": cat})


        # return redirect()