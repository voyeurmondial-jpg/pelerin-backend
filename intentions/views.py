from rest_framework.views import APIView
from rest_framework.response import Response
import requests, os

class GenerateIntention(APIView):
    def post(self, request):
        prompt = request.data.get("prompt")

        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={os.getenv('GEMINI_API_KEY')}",
            json={
                "contents":[{"parts":[{"text":prompt}]}]
            }
        )
        return Response(response.json())
