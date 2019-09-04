from django.http import HttpResponse

def index(request):
    return HttpResponse("Docker! up and running!")