from django.urls import path
from . import views

app_name = "order"
urlpatterns = [
    path('myorders/', views.MyOrdersView.as_view(), name='myorder'),
    path('delete/<int:order_id>/', views.DelOrder.as_view(), name='delorder'),
    # path('pay/', views.PayOrder.as_view(), name='payorder')

]
