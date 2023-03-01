from django.db import models
from home.models import ProductModel
from accounts.models import UserModel


class OrderModel(models.Model):
    """ a model for saving open orders( orders that are just in cart) """
    pro_order = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="order_pro")
    order_size = models.CharField(max_length=50, blank=True, null=True)
    user_order = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="order_user")


class Paymodel(models.Model):
    """when a client pay money for buy product"""
    pro_orders = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="order_proo")
    order_sizes = models.CharField(max_length=50, blank=True, null=True)
    user_orders = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="order_userr")
