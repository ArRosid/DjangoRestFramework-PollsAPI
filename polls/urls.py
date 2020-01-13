from django.urls import path
from rest_framework.routers import DefaultRouter

from . import apiviews

router = DefaultRouter()
router.register('polls', apiviews.PollViewSet, basename="polls")

urlpatterns = [
    # path("polls/", apiviews.PollList.as_view(), name="poll_list"),
    # path("polls/<int:pk>/", apiviews.PollDetail.as_view(), name="poll_detail"),
    # path("choices/", apiviews.ChoiceList.as_view(), name="choice_list"),
    # path("vote/", apiviews.CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/", apiviews.ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:poll_pk>/choices/<int:choice_pk>/vote/", apiviews.CreateVote.as_view(), name="create_vote"),
    path("users/", apiviews.UserCreate.as_view(), name="user_create"),
] 

urlpatterns += router.urls