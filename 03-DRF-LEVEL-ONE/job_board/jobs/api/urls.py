from django.urls import path
from jobs.api.views import (JobOfferListCreateAPIView,
                            JobOfferDetailAPIView)

urlpatterns = [
    path("jobs", 
         JobOfferListCreateAPIView.as_view(),
         name="job-list"),
    path("jobs/<int:pk>", 
         JobOfferDetailAPIView.as_view(),
         name="job-detail"),
]