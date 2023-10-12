from django.shortcuts import render
from .models import Adress
from .models import Resident
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_resendsrefac.services import AdressServices
from app_resendsrefac.services import ResidentServices
from app_resendsrefac.serializers import AdressSerializer
from app_resendsrefac.serializers import ResidentSerializer

