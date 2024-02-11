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

def run_get_recommendation(request):
    seed_track = request.POST.get('track_id')
    seed_artist = request.POST.get('artist_id')
    token = request.session['api__token']
    result_recommendation = Call.get_recommendation(limit=100, seed_track=seed_track, seed_artist=seed_artist,token=token )

    return JsonResponse(result_recommendation)

def run_get_features(request):
    result = get_features(request.POST.track_id, request.session['api__token'])

def end(request):
    request.session.clear()
    return render(request,"index.html")