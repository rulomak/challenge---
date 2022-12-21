import pytest
from datetime import datetime
from todo.models import ToDoList
from todo.serializers import ToDoSerializer


@pytest.mark.django_db
def test_todo_creation():
    todo = ToDoList.objects.create(
        title = 'test',
        description = 'descripcion de prueba',
        is_complete = 'True'

    )

    assert todo.title == 'test'
    assert todo.is_complete == 'True'





# serializer test 
class TestTodoSerializer:
    def test_expected_serializer_json(self):
        expected_results = {
            'id': 1,
            'title': 'test1',
            'description': 'descripcion 1',
            'create_at': str(datetime.now()),
            'is_complete': False
        }

        todo = ToDoList(**expected_results)
        results = ToDoSerializer(todo).data

        assert results == expected_results



