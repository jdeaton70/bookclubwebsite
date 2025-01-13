from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def home(request):
	books = Book.objects.all().order_by('date')
	for book in books:
		if book.author.first_name == "TBD":
			book.author.first_name = ""
			book.author.last_name = ""
	return render(request, 'home.html', {'books':books})
