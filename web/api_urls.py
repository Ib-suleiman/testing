from django.urls import path
from .api_views import CreateBook, CreateSchool, RetrieveUpdateDestroyBookView, RetrieveUpdateDestroySchoolView

urlpatterns = [
    path('books', CreateBook.as_view()),
    path('books/<int:pk>/', RetrieveUpdateDestroyBookView.as_view()),
    path('schools', CreateSchool.as_view()),
    path('schools/<int:pk>/', RetrieveUpdateDestroySchoolView.as_view()),
]
