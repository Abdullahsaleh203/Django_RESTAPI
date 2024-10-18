import json
from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    body = request.body 
    data = {}
    try:
        data = json.loads(body) # string of JSON data => Python Dict
    except:
        pass
    print(data)
    # return JsonResponse(data.values())
    return JsonResponse({"massage":"Hello World "})
# request.body

# print(dir(request))
