from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

class CreateUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ListUsersAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        UserID = self.kwargs['UserID']
        try:
            user = User.objects.get(UserID=UserID)
            return user
        except User.DoesNotExist:
            raise NotFound('User not found.')

class CreateBookAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListBooksAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookIDAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        BookID = self.kwargs['BookID']
        try:
            book = Book.objects.get(bookID=BookID)
            return book
        except User.DoesNotExist:
            raise NotFound('User not found.')
        
@api_view(['POST', 'PUT', 'GET'])
def AssignUpdateBookDetails(request, bookID):
    book_details = get_object_or_404(BookDetail, bookID=bookID)

    serializer = BookDetailSerializer(book_details, data=request.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def BorrowBook(request):
    serializer = BorrowedBookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def ReturnBook(request, borrow_id):
    borrowed_book = get_object_or_404(BorrowedBook, id=borrow_id)
    borrowed_book.returnDate = request.data.get('returnDate')
    borrowed_book.save()
    return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def BorrowedBookList(request):
    borrowed_books = BorrowedBook.objects.all()
    serializer = BorrowedBooksListSerializer(borrowed_books, many=True)
    return Response(serializer.data)
