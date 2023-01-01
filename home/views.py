from django.shortcuts import render, redirect
from django.views import View
from home.models import CategoryModel, ProductModel
from home.forms import ProductForm
from order.models import OrderModel


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


class ProductView(View):
    """ a class for showing product page and handel add to cart permission"""
    class_form = ProductForm()

    def get(self, request, pro_id, pro_slug_url):
        pro = ProductModel.objects.get(pk=pro_id)
        sizes_field = pro.pro_sizes.split(',')
        return render(request, 'home/productpage.html', {"pro": pro, "form": self.class_form, "s": sizes_field})

    def post(self, request, pro_id, pro_slug_url):
        a = ProductForm(request.POST)
        if a.is_valid():
            b = a.cleaned_data
            pro = ProductModel.objects.get(pk=pro_id)
            new_record = OrderModel(order_size=b["choose_size"], pro_order=pro, user_order=request.user)
            new_record.save()
        return redirect("home:homepage")

