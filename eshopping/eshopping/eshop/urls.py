
from django.urls import path
from . import views
from .views import productview


urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    
    path('view/<int:pk>/', productview.as_view(), name='view'),
    
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('terms&conditions/', views.terms, name='terms'),
    path('abouteshopping/', views.about, name='about'),
]