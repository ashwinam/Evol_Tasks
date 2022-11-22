from django.forms import ModelForm
from .models import TypeNoteRelease

class TypeForm(ModelForm):
    class Meta:
        model = TypeNoteRelease
        fields = ['type']

