from django.urls import path
from .views import test_view, records
from .views import get_with_valid_driving_licence, populate_with_sample_data, get_all, get_drivers_with_offenses, get_cars_and_their_owners

urlpatterns = [
    path("test_view/", test_view, name="test_view"),
    path("records/", records, name="records")
]


urlpatterns = [
    path("valid_driving_licence/", get_with_valid_driving_licence, name="filter_valid_driving_licence"),
    path("sample_data/", populate_with_sample_data, name="sample_data")
]


urlpatterns = [
    path("valid_driving_licence/", get_with_valid_driving_licence, name="filter_valid_driving_licence"),
    path("sample_data/", populate_with_sample_data, name="sample_data"),
    path("all/", get_all, name="get_all"),
    path("valid_driving_licence/", get_with_valid_driving_licence, name="valid_driving_licence"),
    path("with_offenses/", get_drivers_with_offenses, name="with_offenses"),
    path("cars/", get_cars_and_their_owners, name="cars")
]