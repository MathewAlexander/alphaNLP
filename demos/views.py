from django.shortcuts import render
from demos.models import Demo

def demo_index(request):
    demos = Demo.objects.all()
    context = {
        'demos': demos
    }
    return render(request, 'demo_index.html', context)


def demo_detail(request, pk):
    demo = Demo.objects.get(pk=pk)
    context = {
        'demo': demo
    }
    return render(request, 'demo_detail.html', context)
