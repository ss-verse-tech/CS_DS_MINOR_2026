from django.urls import path
from products import views
urlpatterns = [
    path("product1", views.product_home_page),
    path("productid/<int:id>", views.product_id),
]
