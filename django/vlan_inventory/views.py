from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view
from .models import VLAN
from .serializers import VLANSerializer


class VLANList(generics.ListAPIView):
    """
    Weergave van alle beschikbare VLANs.
    """
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer
    # permission_classes = [IsAuthenticated, ]


class VLANDetail(generics.RetrieveUpdateAPIView):
    """
    Detailweergave van een beschikbaar VLAN.
    """
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer
    # permission_classes = [IsAuthenticated, ]


class CheckVLAN(APIView):
    def get(self, request, format=None):
        """
        Controleer of het VLAN bestaat.
        """
        if request.GET.get('vlan',''):
            get_key = str(request.GET.get('vlan',''))
            try:
                vlan = VLAN.objects.get(name=get_key) # retrieve the user using Mac
            except VLAN.DoesNotExist:
                data={'message' : False} # return false as mac does not exist
                data['validate_msg'] = {'description' : 'VLAN niet gevonden'}
            else:
                data={'message' : True}
                data['validate_msg'] = {'description' : vlan.description} # Otherwise, return True and Switch
            return Response(data)
        else:
            data={'message' : False}
            data['validate_msg'] = {'description' : "Geen VLAN in verzoek gevonden"} # Otherwise, return True and Switch
            return Response(data)

    def post(self, request, format=None):
        """
        Controle van VLAN.
        """
        try:
            get_key = request.data['inputs']['vlan']
        except:
            return Response({'message' : False, 'stub': True, 'validate_msg' : {'description': 'No valid request' } })
        try:
            vlan = VLAN.objects.get(name=get_key) # retrieve the user using Mac
        except VLAN.DoesNotExist:
            data={'message' : False} # return false as mac does not exist
            data['validate_msg'] = {'description' : 'VLAN niet gevonden'}
        else:
            data={'message' : True}
            data['validate_msg'] = {'description' : vlan.description} # Otherwise, return True and Switch
        return Response(data)
