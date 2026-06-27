from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminUserRole
from .filters import ProductFilter

class ProductListCreateView(generics.ListCreateAPIView):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_class = ProductFilter


    search_fields = [
        "name",
    ]

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAdminUserRole()]

        return [AllowAny()]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []   # temporarily allow anyone