from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminUserRole

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []   # Change to [] if you want anyone to view


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes =[]   # Change to [] if needed