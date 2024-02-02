from django.db import models
from django.utils import timezone

class User(models.Model):
    UserID = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    membershipDate = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name
    
class Book(models.Model):
    bookID = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    ISBN = models.IntegerField(max_length=13, unique=True)
    publishedDate = models.DateField()
    
    def __str__(self):
        return self.title

class BookDetails(models.Model):
    detailsID = models.CharField(max_length=50, unique=True)
    bookID = models.ForeignKey(Book, verbose_name=("bookID"), on_delete=models.CASCADE)
    numberOfPages = models.IntegerField()
    publisher = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.detailsID

class BorrowedBooks(models.Model):
    userID = models.ForeignKey(User, verbose_name=("userID"), on_delete=models.CASCADE)
    bookID = models.ForeignKey(Book, verbose_name=("bookID"), on_delete=models.CASCADE)
    borrowDate = models.DateField()
    returnDate = models.DateField()

    def __str__(self):
        return f'{self.bookID} by {self.userID}'