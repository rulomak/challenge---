from rest_framework import routers
from .views import ToDoViewset

router = routers.DefaultRouter()

router.register('todo', ToDoViewset, 'todoview')


urlpatterns = router.urls

