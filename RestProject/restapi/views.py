from .models import Occurrence
from .serializers import OccurrenceSerializer, CreateOccurrenceSerializer, EditOccurrenceSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrAdmin
from django_filters import FilterSet


# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OccurrenceFilter(FilterSet):

    class Meta:
        model = Occurrence
        fields = {
            'owner': ['exact'],
            'category': ['exact'],
            'lat': ['lte', 'gte'],
            'lon': ['lte', 'gte']
        }


class OccurrenceList(generics.ListCreateAPIView):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_class = OccurrenceFilter # filtros disponiveis

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) # Guarda o user ligado como owner (autor) da ocorrencia.

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        # Verifica se o request é um POST. Se for, muda o serializer para o de criacao.
        if self.request.method == 'POST':
            serializer_class = CreateOccurrenceSerializer
        return serializer_class


class OccurrenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [IsOwnerOrAdmin] # Só permite edicao se for o autor ou se for admin.

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        # Verifica se o request é um PUT. Se for, muda o serializer para o de edicao.
        if self.request.method == 'PUT':
            serializer_class = EditOccurrenceSerializer
        return serializer_class



