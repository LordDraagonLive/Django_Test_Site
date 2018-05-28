from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    # passing a dictionary 'content'
    return render(request, 'personal/basic.html', {'content':['If you like to contact me, please email me','buddiadikari@live.com']})
