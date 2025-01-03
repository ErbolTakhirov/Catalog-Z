from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('object_create/', views.object_create_view),
    path('object_create2/', views.object_create_view2),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('object_delete/<int:pk>/', views.object_delete_view, name='delete'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('photo/<int:pk>/', views.object_detail, name='object_detail'),
    path('object/<int:pk>/delete/', views.object_delete_view, name='object_delete'),
]
