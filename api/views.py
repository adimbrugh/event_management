from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializrs import UserSerailizre, EventSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.routers import Response
from django.utils.timezone import now
from rest_framework import filters
from events.models import Event
from .permissions import IsOwner


User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerailizre
    permission_classes = [IsAuthenticated]



class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    searsh_fields = ['title', 'description', 'location']
    ordering_fields = ['date', 'created_at']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'], url_path='upcoming')
    def upcoming_events(self, request):
        upcoming_events = Event.objects.filter(date__gt=now(), is_cancelled=False)
        serializer = self.get_serializer(upcoming_events, many=True)
        return Response(serializer.data)