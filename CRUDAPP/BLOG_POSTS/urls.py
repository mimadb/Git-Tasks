from django.urls import path
from . import views

urlpatterns = [
    path('', views.listview, name='listview'),
    path('view/<int:pk>', views.blogread, name='blogread'),
    path('updt/<int:pk>', views.blogupdate, name='blogupdate'),
    path('del/<int:pk>', views.blogdelete, name='blogdelete'),
    path('write', views.blogcreate, name='blogcreate'),
]