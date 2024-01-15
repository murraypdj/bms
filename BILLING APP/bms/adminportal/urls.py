from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('call_api/', views.call_api, name='call_api'),
    path('view_all/', views.view_all, name='view_all'),
    path('find/<str:customer_id>/', views.find_customer, name='find_customer'),
]