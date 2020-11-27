from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is an officer's history page!")
