from .models import ToDoList
from .serializers import ToDoSerializer
from rest_framework import viewsets, permissions

class ToDoViewset(viewsets.ModelViewSet):    
    queryset = ToDoList.objects.all() 
    permission_classes = [permissions.AllowAny]  # ( filtrar mas adelante  )
    serializer_class =  ToDoSerializer













