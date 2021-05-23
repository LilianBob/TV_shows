from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add_show', views.create),
#     path('show', views.show),
#     path('edit', views.edit),
#     path('edit/go_to_show', views.show_from_edit),
#     path('delete', views.delete),
#     path('show/edit', views.show_edit),
]