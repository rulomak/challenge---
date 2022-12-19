from .models import ToDoList
from .serializers import ToDoSerializer
from rest_framework import viewsets, permissions

from rest_framework import filters

class ToDoViewset(viewsets.ModelViewSet):    
    queryset = ToDoList.objects.all() 
    permission_classes = [permissions.AllowAny]  # ( filtrar mas adelante  )
    serializer_class =  ToDoSerializer

    # filtros 
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'create_at']












