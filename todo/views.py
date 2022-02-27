
from django.http import HttpResponse
# Create your views here.
def app_page(request):
    return HttpResponse("Todo")
