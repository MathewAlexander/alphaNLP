from django.shortcuts import render

# Create your views here.


def hello_world(request):
    for i in range(10000000):
        k=i*i

    return render(request, k, {})