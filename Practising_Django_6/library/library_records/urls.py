from django.urls import path
from .views import CreateBook, CreateMember, CreateStaff, CreateBookStatus

urlpatterns = [
    path('create_book/', CreateBook.as_view(), name='create_book'),
    path('create_member/', CreateMember.as_view(), name='create_member'),
    path('create_staff/', CreateStaff.as_view(), name='create_staff'),
    path('book_status/', CreateBookStatus.as_view(), name='book_status'),
]

