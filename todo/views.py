from .models import ToDoList
from .serializers import ToDoSerializer
from rest_framework import viewsets, permissions

from rest_framework import filters


class ToDoViewset(viewsets.ModelViewSet):    
    permission_classes = [permissions.IsAuthenticated]  
    queryset = ToDoList.objects.all().order_by('-create_at')
    serializer_class =  ToDoSerializer

    # filtros - Busqueda
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'create_at']












