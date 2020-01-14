from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from . import models, serializers


# class PollList(APIView):
#     def get(self, request):
#         pools = models.Poll.objects.all()[:20]
#         data = serializers.PoolSerializer(pools, many=True).data
#         return Response(data)

# class PollDetail(APIView):
#     def get(self, request, pk):
#         poll = get_object_or_404(models.Poll, pk=pk)
#         data = serializers.PoolSerializer(poll).data
#         return Response(data)

# class PollList(generics.ListCreateAPIView):
#     queryset = models.Poll.objects.all()
#     serializer_class = serializers.PoolSerializer

# class PollDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Poll.objects.all()
#     serializer_class = serializers.PoolSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PoolSerializer

    def destroy(self, request, *args, **kwargs):
        poll = models.Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You can not delete this poll!")
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# class ChoiceList(generics.ListCreateAPIView):
#     queryset = models.Choice.objects.all()
#     serializer_class = serializers.ChoiceSerializer

# class CreateVote(generics.CreateAPIView):
#     serializer_class = serializers.VoteSerializer

class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = models.Choice.objects.filter(poll_id=self.kwargs["poll_pk"])
        return queryset
    serializer_class = serializers.ChoiceSerializer

    def perform_create(self, serializer):
        poll = models.Poll.objects.get(pk=self.kwargs["poll_pk"])
        if not self.request.user == poll.created_by:
            raise PermissionDenied("You can not create choice for this poll!")
        serializer.save(poll=poll)

class CreateVote(APIView):
    serializer_class = serializers.VoteSerializer

    def post(self, request, poll_pk, choice_pk):
        voted_by = self.request.user.id
        
        try:
            poll = models.Poll.objects.get(pk=poll_pk)
            choice = models.Choice.objects.get(pk=choice_pk)
            
            if choice.poll != poll:
                return Response({"error_message":"Choices with that poll do not exist"}, status=status.HTTP_400_BAD_REQUEST)
            
            data = {"choice": choice_pk, "poll": poll_pk, "voted_by":voted_by}
            serializer = serializers.VoteSerializer(data=data)
            if serializer.is_valid():
                vote = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error_message":"Poll or Choices do not exist!"}, status=status.HTTP_400_BAD_REQUEST)

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.UserSerializer

class LoginView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


