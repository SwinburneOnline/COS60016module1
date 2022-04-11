
from django.urls import path
# All the class based views will need to be imported
from basic_calculator.views import AddView, SubView, DivView, MultiView

# All the classes will be used as views and each one will have a path defined.

urlpatterns = [
    path('add/', AddView.as_view()),
    path('sub/', SubView.as_view()),
    path('div/', DivView.as_view()),
    path('multi/', MultiView.as_view()),
]

