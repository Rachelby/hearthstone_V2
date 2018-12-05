from django.urls import path

from . import views

urlpatterns = [
    # ex: /cards/
    path('', views.index, name='index'),
    
    # ex: /cards/list
    path('list', views.list, name='list'),

    # ex: /cards/5/
    path('<int:card_id>/', views.detail, name='detail'),
    
    # ex: /cards/5/edit/
    path('<int:card_id>/edit/', views.edit, name='edit'),

]