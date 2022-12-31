from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('category/<slug:cat_slug_url>/',
         views.CategoryView.as_view(), name='categorypage')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
