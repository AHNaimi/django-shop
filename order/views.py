from django.shortcuts import render, redirect
from django.views import View
from .models import OrderModel, Paymodel
from home.models import ProductModel
from django.contrib import messages


class MyOrdersView(View):
    """ because of this class customer can see all products
                              that already add to cart and can delete them """

    def get(self, request):
        if request.user.is_authenticated:
            user_orders = OrderModel.objects.filter(user_order=request.user).values()
            all_pay = 0
            pro = []
            for x in user_orders:
                s = ProductModel.objects.get(pk=x['pro_order_id'])
                r = s.pro_price
                all_pay += int(r)
                pro.append(ProductModel.objects.get(pk=x["pro_order_id"]))
            proder = zip(pro, user_orders)
            return render(request, "order/myorders.html", {"proder": proder, "all_pay": all_pay})
        else:
            messages.info(request, "you have to register in site first")
            return redirect("accounts:register")

    def post(self, request):
        user_orders = OrderModel.objects.filter(user_order=request.user).values()
        user_orm = OrderModel.objects.filter(user_order=request.user)
        for x in user_orm:
            new_record = Paymodel(pro_paid=x)
            new_record.save()
            x.delete()
        return redirect("order:myorder")


class DelOrder(View):
    """ a class for handling delete orders"""

    def get(self, request, order_id):
        pro = OrderModel.objects.get(id=order_id)
        pro.delete()
        messages.info(request, "product removed from your Cart")
        return redirect('order:myorder')



