from django.urls import path
from . import views

urlpatterns = [
    path('',views.registration, name='home'),
    path('add_invoice/', views.add_invoice, name="add_invoice"),
    path('list_invoice/',views.list_invoices, name='list_invoices'),
    path('update_invoice/<str:pk>/', views.update_invoice, name='update_invoice'),
    path('delete/<int:pk>/', views.delete_invoice, name='delete_invoice'),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.my_logout,name='logout')
]
