from django.shortcuts import render

# Create your views here.
def partners(request):
    return render(request, 'partnersapp/index.html')
