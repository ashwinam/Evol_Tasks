from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .forms import TypeForm
from .models import TypeNoteRelease


class TypeView(generic.ListView):
    model = TypeNoteRelease
    template_name: str = 'index.html'
    context_object_name: str = 'objects'

class TypeCreate(generic.CreateView):
    model = TypeNoteRelease
    template_name: str = 'create.html'
    form_class = TypeForm
    success_url: str = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context

    def post(self, request, *args: str, **kwargs):
        form = TypeForm(request.POST)
        if form.is_valid:
            note_type = request.POST['type']
            try:
                query_type = TypeNoteRelease.objects.get(type__contains=note_type).type
            except TypeNoteRelease.DoesNotExist:
                query_type = None
            if query_type:
                messages.error(request, "The type is already exists, please add new one.")
                return redirect('create')

                # return super().post(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)


class TypeUpdate(generic.UpdateView):
    model = TypeNoteRelease
    # fields = ['type']
    form_class = TypeForm
    template_name: str = 'create.html'
    success_url: str = '/'

    def post(self, request, *args: str, **kwargs):
        form = TypeForm(request.POST)
        if form.is_valid:
            note_type = request.POST['type']
            rec_id = request.POST['rec_id']
            print('-----------',note_type)

            ans = TypeNoteRelease.objects.filter()
            print('->>>>>>>>>',ans)

            # pk_id = TypeNoteRelease.objects.get(type=note_type).type_id

            # queryset = TypeNoteRelease.objects.exclude(type=query_type).values_list('type', flat=True)
            if TypeNoteRelease.objects.filter(type_id=rec_id).exclude(type=note_type).exists():
                messages.error(request, "Duplicate Type.")
                return redirect('update', pk=kwargs['pk'])
                # return redirect('create')

        return super().post(request, *args, **kwargs)


class TypeDelete(generic.DeleteView):
    model = TypeNoteRelease
    success_url: str = '/'
    template_name: str = 'confirm_delete.html'
    