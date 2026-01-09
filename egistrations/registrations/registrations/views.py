from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Registration
from .serializers import RegistrationSerializer
import random

class RegisterPilgrim(APIView):
    def post(self, request):
        data = request.data.copy()
        data['pelerin_id'] = f"PEL-2026-{random.randint(1000,9999)}"

        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
