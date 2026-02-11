from rest_framework import generics
from .serializers import BookSerializer, SchoolSerializer
from .models import Book, School
from rest_framework.permissions import IsAdminUser

class CreateBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class RetrieveUpdateDestroyBookView(generics. RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

class CreateSchool(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAdminUser]


class RetrieveUpdateDestroySchoolView(generics.RetrieveDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAdminUser]


    