from django.contrib import admin

from subtask_app.models import Subtask
from .models import Todos

# Register your models here.

admin.site.register(Todos)
