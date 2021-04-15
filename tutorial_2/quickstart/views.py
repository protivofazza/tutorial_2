from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UsersSerializer, TariffsSerializer, StatesSerializer
from .models import Users, Tariffs, States


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('family_name')
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


class TariffsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tariffs.objects.all()
    serializer_class = TariffsSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = States.objects.all()
    serializer_class = StatesSerializer
    permission_classes = [permissions.IsAuthenticated]