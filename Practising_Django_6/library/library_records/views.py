from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from .models import BookStatus, Book, Member, Staff


# Create your views here.

class CreateBook(View):
    def post(self, request):
        book = Book(title=request.POST['title'], description=request.POST['description'], author=request.POST['author'])
        book.save()
        my_book = Book.objects.all().filter(title=request.POST['title'])
        if my_book:
            return HttpResponse(status=200)
        return HttpResponse("Book not saved", status=404)



class CreateMember(View):
    def post(self, request):
        member = Member(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
        member.save()
        my_member = Member.objects.all().filter(first_name=request.POST['first_name'])
        if my_member:
            return HttpResponse(status=200)
        return HttpResponse("Member not saved", status=404)



class CreateStaff(View):
    def post(self, request):
        staff = Staff(first_name=request.POST['first_name'], last_name=request.POST['last_name'], age=request.POST['age'], position=request.POST['position'])
        staff.save()
        my_staff = Staff.objects.all().filter(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
        if my_staff:
            return HttpResponse(status=200)
        return HttpResponse("Staff not saved", status=404)





class CreateBookStatus(View):
    def post(self, request):
        # DELETE AFTER TESTING
        member = Member(first_name="Clara", last_name="Clark")
        member.save()


        staff = Staff(first_name="Laura", last_name="Clark",
                      age=27, position="librarian")
        staff.save()


        book = Book(title="Random Books", description="This is an awesome random book", author="John Doe")
        book.save()
        ####


        book = Book.objects.all().filter(title=request.POST['book_title']).first()
        member = Member.objects.all().filter(first_name=request.POST['member_name'], last_name=request.POST['member_last_name']).first()
        staff = Staff.objects.all().filter(first_name=request.POST['staff_name'], last_name=request.POST['staff_last_name']).first()

        if book and member and staff:
            book_status = BookStatus(status=(request.POST['status01'], request.POST['status02']), book=book, issued_by=staff, issued_to=member)
            book_status.save()
            status = BookStatus.objects.all().filter(status=(request.POST['status01'], request.POST['status02']),
                                                     book=book)
        else:
            return HttpResponse("Status not updated constraints not found", status=204)


        if status:
            return HttpResponse(status=200)
        return HttpResponse("Status not updated", status=404)
    