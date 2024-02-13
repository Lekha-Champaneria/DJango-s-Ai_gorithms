from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .process_functions import Call
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is homepage")

def run_get_token(request):
    request.session['api__token'] = Call.get_token()
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
    track_id = request.POST.get('track_id')
    access_token = request.session.get('api__token')
    print("*******************************************", track_id, " ", access_token)
    result = Call.get_features(track_id=track_id, access_token=access_token)
    print(result)
    return JsonResponse(result)

def run_get_top10(request):
    Target_track = request.POST.get('_target_track')
    Target_track_features = request.POST.get('_target_features')
    _100Tracks = request.POST.get('_100tracks')
    _100Features = request.POST.get('_100features')
    response = Call.get_top10(
        targetFeatures=Target_track_features,
        target_track=Target_track,
        _100Features=_100Features,
        _100Tracks=_100Tracks
    )
    return JsonResponse(response)

def end(request):
    request.session.clear()
    return render(request,"index.html")