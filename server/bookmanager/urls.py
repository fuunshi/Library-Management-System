from django.urls import path
from .views import *

urlpatterns = [
    path('create-user/', CreateUserAPIView.as_view(), name='create-user'),
    path('users/', ListUsersAPIView.as_view(), name='list-users'),
    path('users/<str:UserID>/', UsersDetailAPIView.as_view(), name='user-detail'),
    path('create-book/', CreateBookAPIView.as_view(), name='create-book'),
    path('books/', ListBooksAPIView.as_view(), name='list-books'),
    path('books/<str:BookID>/', BookIDAPIView.as_view(), name='get-book'),
    path('book-details/<int:bookID>/', AssignUpdateBookDetails, name='assign-update-book-details'),
    path('borrow-book/', BorrowBook, name='borrow-book'),
    path('return-book/<int:borrow_id>/', ReturnBook, name='return-book'),
    path('list-borrowed-books/', BorrowedBookList, name='borrowed-books'),
]
