import json
from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    # print(request.POST)
    body = request.body 
    data = {}
    try:
        data = json.loads(body) # string of JSON data => Python Dict
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    print(f'request .GET = {request.GET}')
    print(f'request .POST = {request.POST}')
    print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
    # return JsonResponse({"massage":"Hello World "})
# request.body

# print(dir(request))
