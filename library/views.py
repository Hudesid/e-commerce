from rest_framework import generics
from .serializer import BookSerializer, Book

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
