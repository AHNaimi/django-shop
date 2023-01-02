from django.shortcuts import render
from django.views import View
from .models import OrderModel
from home.models import ProductModel

class MyOrdersView(View):
    """ because of this class customer can see all products
                              that already add to cart and can delete them """
    def get(self, request):
        user_orders = OrderModel.objects.filter(user_order=request.user).values()
        pro = []
        for x in user_orders:
            pro.append(ProductModel.objects.get(pk=x["pro_order_id"]))
        proder = zip(pro, user_orders)
        return render(request, "order/myorders.html", {"proder": proder})
