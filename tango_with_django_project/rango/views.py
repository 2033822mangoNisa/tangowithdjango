from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! </br> <a href = '/rango/about'> About </a>")

def about(request):
    return HttpResponse("Rango says: Here is the about page! </br>"
                        + "This tutorial has been put togeather by Waqar-un-nisa Nabi, 2033822N"
                        + "<br/> <a href='/rango/'> Index </a>")
