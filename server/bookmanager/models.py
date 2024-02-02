from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    membershipDate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    bookID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    publishedDate = models.DateField()
    genre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class BookDetail(models.Model):
    detailsID = models.AutoField(primary_key=True)
    bookID = models.OneToOneField(Book, verbose_name=("bookID"), on_delete=models.CASCADE)
    numberOfPages = models.IntegerField()
    publisher = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.detailsID}"

class BorrowedBook(models.Model):
    userID = models.ForeignKey(User, verbose_name=("userID"), on_delete=models.CASCADE)
    bookID = models.ForeignKey(Book, verbose_name=("bookID"), on_delete=models.CASCADE)
    borrowDate = models.DateField()
    returnDate = models.DateField()

    def __str__(self):
        return f"{self.UserID.name} borrowed {self.BookID.title}"