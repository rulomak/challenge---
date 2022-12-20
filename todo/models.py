from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.title




