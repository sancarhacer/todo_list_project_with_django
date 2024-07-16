from django.db import models
from todo_app.models import Todos

from datetime import datetime




# Create your models here.

#related_name ile Todos modelinden Subtask modeline erişmek için kullanılacak ilişki adını belirtirsin.
#blank=False: Formlar aracılığıyla veri girilirken bu alanın boş bırakılmaması gerektiğini belirtir. Bu, kullanıcı arayüzünden gelen veriler için geçerlidir.
#null=False: Veritabanında bu alanın boş (null) olamayacağını belirtir. Bu, veritabanı düzeyindeki doğrulamadır.

class Subtask (models.Model):
    todo = models.ForeignKey(Todos, on_delete=models.CASCADE,related_name='subtasks')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank = True)
    finished = models.BooleanField(default = False)
    date = models.DateField(default=datetime.now, blank =True)

    def __str__(self):
        return self.title
    