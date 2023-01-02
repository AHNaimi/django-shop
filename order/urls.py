from django.urls import path
from . import views

app_name = "order"
urlpatterns = [
    path('myorders/', views.MyOrdersView.as_view(), name='myorder'),

]
