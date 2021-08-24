from django.urls import path

from books_api import views

urlpatterns = [
    path('', views.BookListCreate.as_view()),
    path('<int:book_id>', views.BookGedUpdateDelete.as_view())
]