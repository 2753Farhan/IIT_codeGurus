from django.urls import path
from . import views

urlpatterns = [
    path('', views.step1, name='step1'),  # This is the root URL pattern
    path('step2/<str:state>/<str:country>/<str:selected_city>/', views.step2, name='step2'),
]
