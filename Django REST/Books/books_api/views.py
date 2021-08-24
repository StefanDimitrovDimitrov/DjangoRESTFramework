from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from books_api.models import BookModel
from books_api.serializers import BookSerializer


class BookListCreate(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGedUpdateDelete(APIView):
    def put(self,request, book_id):
        pass

    def get(self, request, book_id):
        book = BookModel.objects.get(id=book_id)
        if book:
            book_serializer = BookSerializer(book)
            return Response(book_serializer.data)
        return Response({"message": "Not found"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        pass