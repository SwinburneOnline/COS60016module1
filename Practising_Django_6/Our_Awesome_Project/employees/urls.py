from django.urls import path, include
from .views import show_all, order_by_location, populate_with_sample_data, order_by_role



urlpatterns = [
    path("show_all/", show_all, name="show_all"),
    path("sample_data/", populate_with_sample_data, name="sample_data"),
    path("order_by_location/", order_by_location, name="order_by_location"),
    path("order_by_role/", order_by_role, name="order_by_role"),
]