from django.db import models



# Create your models here.

#a Book model that will hold data about the books
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    author = models.CharField(max_length=50)
    def __str__(self): #function will return the name of the class
        return self.title

#Staff model, which will hold information about the staff that work in the library
class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    def __str__(self): #function will return the name of the class
        return self.first_name + " " + self.last_name


#a ‘Member’ class, which will hold the first_name and last_name of a library member who will take out books
class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    def __str__(self): #function will return the name of the class
        return self.first_name + " " + self.last_name


#BookStatus model will be used to store status information about books so that we know who the book was issued to and by whom
class BookStatus(models.Model):
    book_status_choices = [('Rented', 'Rented'),
                           ('Not-Rented', 'Not-Rented')]


    status = models.CharField(max_length=50, choices=book_status_choices)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    issued_by = models.OneToOneField(Staff, on_delete=models.CASCADE)
    issued_to = models.OneToOneField(Member, on_delete=models.CASCADE)
    def __str__(self): #function will return the name of the class
        return "Book Status"

