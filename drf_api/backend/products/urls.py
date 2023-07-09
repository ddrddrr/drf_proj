from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductUpdateView, ProductDestroyView

urlpatterns = [
    path("", ProductListCreateView.as_view()),
    path("<int:pk>/update/", ProductUpdateView.as_view()),
    path("<int:pk>/delete/", ProductDestroyView.as_view()),
    path("<int:pk>/", ProductDetailView.as_view()),
]
