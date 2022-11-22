from django.db import models

# Create your models here.

class TypeNoteRelease(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.type