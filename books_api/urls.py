from django.urls import path
from books_api import views


urlpatterns = [
    path('', views.BookListCreate.as_view()),
    path('<int:pk>', views.BookGetUpdateDelete.as_view()),

]