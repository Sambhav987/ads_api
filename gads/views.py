from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'var': "this is var 1"
    }
    # return render(request, 'index.html', context)
    return HttpResponse("this is Gads homepage")
