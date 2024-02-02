from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UserID', 'name', 'email', 'membershipDate']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bookID', 'title', 'ISBN', 'publishedDate', 'genre']

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields = ['numberOfPages', 'publisher', 'language']

class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ['userID', 'bookID', 'borrowDate', 'returnDate']

class BorrowedBooksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ['id', 'userID', 'bookID', 'borrowDate', 'returnDate']