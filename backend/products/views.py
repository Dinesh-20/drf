from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(UserQuerySetMixin,generics.ListCreateAPIView,StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated():
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)

class ProductDetailAPIView(UserQuerySetMixin,generics.RetrieveAPIView,StaffEditorPermissionMixin):
    # in detail view of any kind we can set a lookup on a field for database searches.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(UserQuerySetMixin,generics.UpdateAPIView,StaffEditorPermissionMixin):
    # in update view also of any kind we can set a lookup on a field for database searches.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(UserQuerySetMixin,generics.DestroyAPIView,StaffEditorPermissionMixin):
    # in update view also of any kind we can set a lookup on a field for database searches.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# this is the actual implementation of the generic views inherited above.


@api_view(["GET","POST"])
def product_alt_view(request, pk=None,*args, **kwargs):
    method = request.method

    if method=='GET':
        if pk is not None:
            # do get request -> detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method=="POST":
        # do post method -> create view
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'invalid':'bad input'}, status=400)
    
