from django.urls import path
from . import views, views2

urlpatterns = [
    path('', views.index, name='index'),
    path('city/<str:state>/<str:country>/<str:city>/', views2.city_detail, name='city_detail'),
]
