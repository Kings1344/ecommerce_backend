from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    # GET all + POST new category
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),

    # GET / PUT / DELETE single category
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]