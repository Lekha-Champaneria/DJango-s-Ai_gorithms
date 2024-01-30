from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .process_functions import Call
# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is homepage")

def run_get_token(request):
    request.session['api__token'] = Call.get_token()
    # return render(request, "index.html")
    return HttpResponseRedirect("/")

# def end(request):
#     request.session.clear()
#     return render(request,"index.html")