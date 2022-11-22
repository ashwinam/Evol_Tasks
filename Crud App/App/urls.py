from django.urls import path
from . import views

urlpatterns = [
    path('', views.TypeView.as_view(), name='index'),
    path('create/', views.TypeCreate.as_view(), name='create'),
    path('update/<int:pk>', views.TypeUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.TypeDelete.as_view(), name='delete'),
]

