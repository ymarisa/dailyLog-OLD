from django.shortcuts import render
from django.contrib.auth.models import User
from log.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import permissions
from log.models import Log, Habit
from log.serializers import LogSerializer, HabitSerializer, UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'habits': reverse('user-habits', request=request, format=format)
    })


# List / Create views
class LogList(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    # permission_classes = [permissions.IsAuthenticated]


class HabitList(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Retrieve, update or delete a log or habit instance
class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    # permission_classes = [permissions.IsAuthenticated] ## TODO: fix permissions here?


class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


