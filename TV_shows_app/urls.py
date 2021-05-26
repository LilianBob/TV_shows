from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new_show),
    path('add_show', views.create),
    path('back', views.back),
    path('show/<int:show_id>', views.show),
    path('edit/<int:show_id>', views.edit),
    path('update/<int:show_id>', views.update),
#     path('edit/go_to_show', views.show_from_edit),
    path('delete/<int:show_id>', views.delete),
#     path('show/edit', views.show_edit),
]