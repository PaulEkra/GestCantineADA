from django.urls import path
from menu import views

app_name = 'menu'
urlpatterns = [

    path('', views.list_menu, name='list'),
    path('add/', views.add_menu, name='add'),
    path('edit/<int:id>', views.edit_menu, name='edit'),
    path('delete/<int:id>', views.delete_menu, name='delete'),

]