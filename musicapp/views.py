from django.shortcuts import render
from django.views.generic import ListView
from musicapp.models import Song
# Create your views here.

class SongView(ListView):
    model = Song
    
