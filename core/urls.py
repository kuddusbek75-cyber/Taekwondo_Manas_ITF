from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]