from django.urls import path
from . import apiviews

urlpatterns = [
    path("polls/", apiviews.PollList.as_view(), name="poll_list"),
    path("polls/<int:pk>/", apiviews.PollDetail.as_view(), name="poll_detail"),
    path("choices/", apiviews.ChoiceList.as_view(), name="choice_list"),
    path("vote/", apiviews.CreateVote.as_view(), name="create_vote")
]