from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

import json


@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    '''
    DRF API VIEW
    '''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({'invalid':'not good data'}, status=400)

    # this is the underlyong process of Serialization
    # get model and data from it
    # convert into python dictionary
    # send it as JSON to client.
    # if model_data:
    #     data['id']=model_data.id
    #     data['title']=model_data.title
    #     data['content']=model_data.content
    #     data['price']=model_data.price
    

