from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Youth
from youth import serializers

class YouthViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.YouthSerializer
    queryset = Youth.objects.all()
    authentication_classes = [TokenAuthentication]
    authentication_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user).order_by('-id')
