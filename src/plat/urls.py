from django.urls import path
from plat import views

app_name = 'plat'
urlpatterns = [
    
    path('', views.list_plat, name='list'),
    path('add/', views.add_plat, name='add'),
    path('edit/<int:id>', views.edit_plat, name='edit'),
    path('delete/<int:id>', views.delete_plat, name='delete'),

]