from django.shortcuts import render
from rest_framework import generics


# Create your views here.
from .models import Game
from .serializers import GameSerializer

class ListGame(generics.ListAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer

class DetailGame(generics.RetrieveAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer

