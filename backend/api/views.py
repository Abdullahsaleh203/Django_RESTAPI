import json
from django.http import JsonResponse , HttpRequest
from django.forms.models import model_to_dict
from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data =model_to_dict(model_data, fields=['id','title','content'])
    return HttpRequest(data, headers={"content-type":"application/json"})
    # return JsonResponse(data)

