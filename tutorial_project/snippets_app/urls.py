from django.urls import path
from snippets_app import views

urlpatterns = [
    path('snippets', views.snippet_list, name='snippet_list'),
    path('snippets/<int:pk>/', views.snippet_detail, name='snippet_detail'),
    ]