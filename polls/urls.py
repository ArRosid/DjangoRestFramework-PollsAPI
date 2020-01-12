from django.urls import path
from . import apiviews

urlpatterns = [
    path("polls/", apiviews.PollList.as_view(), name="poll_list"),
    path("polls/<int:pk>/", apiviews.PollDetail.as_view(), name="poll_detail")
]