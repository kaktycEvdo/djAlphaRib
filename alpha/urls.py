from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('reg/', views.RegView.as_view(), name='reg'),
    path('auth/', views.AuthView.as_view(), name='auth'),
    path('favs/', views.favs, name='favs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
