from django.urls import path
from . import views

#from .views import PageView


urlpatterns = [
    #path(r'admin/', admin.site.urls),
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    # Need to have user urls as well
    #path('users/login/', views.store, name="store"),
]