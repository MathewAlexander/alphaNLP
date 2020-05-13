from django.shortcuts import render
from ip2geotools.databases.noncommercial import DbIpCity


# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip





def hello_world(request):
    ip=get_client_ip(request)

    data = DbIpCity.get(str(ip), api_key='free')
    address=data.to_json()



    return render(request, 'hello_world.html', {"address":address})