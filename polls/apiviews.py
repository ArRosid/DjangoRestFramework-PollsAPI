from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

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

# class ChoiceList(generics.ListCreateAPIView):
#     queryset = models.Choice.objects.all()
#     serializer_class = serializers.ChoiceSerializer

# class CreateVote(generics.CreateAPIView):
#     serializer_class = serializers.VoteSerializer

class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = models.Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = serializers.ChoiceSerializer

class CreateVote(APIView):
    serializer_class = serializers.VoteSerializer

    def post(self, request, poll_pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {"choice": choice_pk, "poll": poll_pk, "voted_by":voted_by}
        serializer = serializers.VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreate(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer