from rest_framework import serializers
from rest_framework.reverse import reverse
from .validators import validate_title

from api.serializers import UserPublicSerializer

from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
            'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'path',
            'endpoint'
        ]

    # to create custom validators
    # def validate_<fieldname>
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("Title already exists")
    #     return value 
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if not request:
            return None
        return reverse('product-edit', kwargs={'pk':obj.pk}, request=request)


    def get_my_discount(self, obj):# this obj -> insatnce of model itself
        try:
            return obj.get_discount()
        except:
            None