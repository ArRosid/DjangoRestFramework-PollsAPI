from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

from . import apiviews

router = DefaultRouter()
router.register('polls', apiviews.PollViewSet, basename="polls")

urlpatterns = [
    # path("polls/", apiviews.PollList.as_view(), name="poll_list"),
    # path("polls/<int:pk>/", apiviews.PollDetail.as_view(), name="poll_detail"),
    # path("choices/", apiviews.ChoiceList.as_view(), name="choice_list"),
    # path("vote/", apiviews.CreateVote.as_view(), name="create_vote"),
    path("polls/<int:poll_pk>/choices/", apiviews.ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:poll_pk>/choices/<int:choice_pk>/vote/", apiviews.CreateVote.as_view(), name="create_vote"),
    path("users/", apiviews.UserCreate.as_view(), name="user_create"),
    # path("login/", apiviews.LoginView.as_view(), name="login"),
    # path("login/", views.obtain_auth_token, name="login"),
    path('docs/', include_docs_urls(title="Polls API", permission_classes=())),
    path('api-auth/',
        include("rest_auth.urls")),
] 

urlpatterns += router.urls