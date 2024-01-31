from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .process_functions import Call
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is homepage")

def run_get_token(request):
    request.session['api__token'] = Call.get_token()
    # return render(request, "index.html")
    return HttpResponseRedirect("/")
    
def run_get_song_details(request):
    query = request.POST.get('q')
    token = request.POST.get('token')
    track = Call.get_song_details(query, token)
    
    # return render(request, "index.html")
    return JsonResponse(track)

def end(request):
    request.session.clear()
    return render(request,"index.html")