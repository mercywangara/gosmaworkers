from django.urls import path
from . import views

urlpatterns = [
    path('', views.members_dashboard, name='home'),
    path('members/', views.members_dashboard, name='members_dashboard'),
    path('savings/', views.savings_dashboard, name='savings_dashboard'),
    path('transactions/', views.transactions_dashboard, name='transactions_dashboard'),
]