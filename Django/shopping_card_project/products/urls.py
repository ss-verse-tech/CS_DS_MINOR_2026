from django.urls import path, re_path
from products import views
urlpatterns = [
    path("product1", views.product_home_page),
    path("productid/<int:id>/<str:name>/<int:age>", views.product_id),
    re_path(r'^show_year/(?P<year>[0-9]{4})/$', views.show_year),
]
