from rest_framework import generics
from .models import Product
from .serializers import FullProductSerializer
from drf_api.backend.actual_api.mixins import StaffEditorPermissionMixin


class ProductDetailView(generics.RetrieveAPIView,
                        StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = FullProductSerializer


class ProductListCreateView(generics.ListCreateAPIView,
                            StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = FullProductSerializer

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content")
        if content is None:
            content = "content unknown"
        print(serializer)
        serializer.save(content=content)


class ProductDestroyView(generics.DestroyAPIView,
                         StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = FullProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ProductUpdateView(generics.UpdateAPIView,
                        StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = FullProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        if serializer.is_valid():
            instance = serializer.save()
            if not instance.content:
                instance.content = "no content available"
                instance.save()
