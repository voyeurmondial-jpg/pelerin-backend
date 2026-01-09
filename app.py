import os
import json
import uuid
from datetime import datetime

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient

# ================================
# DJANGO SETTINGS MINIMAUX
# ================================
if not settings.configured:
    settings.configure(
        DEBUG=os.environ.get("DEBUG", "False") == "True",
        SECRET_KEY=os.environ.get("SECRET_KEY", "django-insecure-pelerin-2026"),
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["*"],
        MIDDLEWARE=[],
    )

# ================================
# MONGODB CONNECTION
# ================================
MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["pelerin_db"]
collection = db["pelerins"]

# ================================
# VIEWS / API
# ================================
def home(request):
    return JsonResponse({
        "status": "online",
        "service": "Pèlerin Connect API",
        "time": datetime.utcnow().isoformat()
    })

@csrf_exempt
def pelerins(request):
    if request.method == "GET":
        data = list(collection.find({}, {"_id": 0}))
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        body = json.loads(request.body)

        if not body.get("nom") or not body.get("prenom"):
            return JsonResponse({"error": "Nom et prénom obligatoires"}, status=400)

        pilgrim = {
            "officialId": f"PEL-{uuid.uuid4().hex[:6].upper()}",
            "nom": body["nom"],
            "prenom": body["prenom"],
            "present": False,
            "statut": "PAYE",
            "createdAt": datetime.utcnow()
        }

        collection.insert_one(pilgrim)
        pilgrim.pop("_id", None)

        return JsonResponse(pilgrim, status=201)

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def presence(request, official_id):
    if request.method == "PATCH":
        result = collection.update_one(
            {"officialId": official_id},
            {"$set": {"present": True}}
        )

        if result.matched_count == 0:
            return JsonResponse({"error": "Pèlerin introuvable"}, status=404)

        return JsonResponse({"message": "Présence validée"})

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

# ================================
# URLS
# ================================
urlpatterns = [
    path("", home),
    path("api/pelerins", pelerins),
    path("api/pelerins/<str:official_id>/presence", presence),
]

# ================================
# WSGI
# ================================
application = get_wsgi_application()

# ================================
# RUN LOCAL
# ================================
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    import sys
    execute_from_command_line(sys.argv)
