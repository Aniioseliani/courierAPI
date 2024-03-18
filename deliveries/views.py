from rest_framework import viewsets
from .models import CustomUser, Parcel, DeliveryProof
from .serializers import CustomUserSerializer, ParcelSerializer, DeliveryProofSerializer

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
class ParcelViewset(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    
class DeliveryProofViewset(viewsets.ModelViewSet):  # Corrected class name
    queryset = DeliveryProof.objects.all()
    serializer_class = DeliveryProofSerializer


    
