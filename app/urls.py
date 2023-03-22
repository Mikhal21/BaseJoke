from django.urls import path
from . import views
 
app_name='app'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('entry/<int:id>/', views.get_user_entry, name='get_user_entry'),
]
