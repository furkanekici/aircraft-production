from django.shortcuts import render
from .models import Team
from .serializers import TeamSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from users.models import Personnel

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    # List only teams associated with the current user's personnel
    def get_queryset(self):
        user_personnel = self.request.user
        return Team.objects.filter(personnel=user_personnel)

    # Custom action to manage personnel within teams
    @action(detail=True, methods=['post'], url_path='add-personnel', permission_classes=[IsAuthenticated])
    def add_personnel(self, request, pk=None):
        """
        Custom action to add personnel to a team.
        """
        team = get_object_or_404(Team, pk=pk)
        personnel_id = request.data.get('personnel_id')

        personnel = get_object_or_404(Personnel, id=personnel_id)
        team.personnel.add(personnel)
        return Response({'status': 'personnel added'})

    @action(detail=True, methods=['post'], url_path='remove-personnel', permission_classes=[IsAuthenticated])
    def remove_personnel(self, request, pk=None):
        """
        Custom action to remove personnel from a team.
        """
        team = get_object_or_404(Team, pk=pk)
        personnel_id = request.data.get('personnel_id')

        personnel = get_object_or_404(Personnel, id=personnel_id)
        team.personnel.remove(personnel)
        return Response({'status': 'personnel removed'})
