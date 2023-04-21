from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_store),
    path('index', views.show, name='all_stores'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
