from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("upload_product/", views.upload_product, name="upload_product"),
    path("product_page/", views.product_page, name="product_page"),
    path("order/", views.order, name="order"),
]