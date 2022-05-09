import firebase_admin
from firebase_admin import credentials, firestore
from django.shortcuts import render
cred = credentials.Certificate("D:\Projects\PX hardware\park_xplore\web\serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# Create your views here.
def home(request):
    return render(request, 'index.html')


def occupied(request, slug):
    parking = db.collection(u'parking_slots').document(slug)
    parking.update({u'status': "Occupied"})
    return render(request, 'index.html')


def free(request, slug):
    parking = db.collection(u'parking_slots').document(slug)
    parking.update({u'status': "free"})
    return render(request, 'index.html')


# 251c5140-c8a3-11ec-9ee0-af43e4fd9d71
# 979a6d20-c8a2-11ec-9ee0-af43e4fd9d71
# d4baf510-c476-11ec-9ebd-4f842fec3f71
