from django.urls import path
from .views import PublisherListView

urlpatterns = [
    path("publishers", PublisherListView.as_view())
]