from django.urls import path
from snippets_app import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('snippets/', SnippetListView.as_view()),
    path('snippets/<int:pk>/', SnippetDetailView.as_view()),
    ]

# Allows us to accept a 'format' parameter as part of a query that specifies the format of the requested response
urlpatterns = format_suffix_patterns(urlpatterns)