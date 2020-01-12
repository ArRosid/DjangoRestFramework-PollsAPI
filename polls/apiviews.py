from django.shortcuts import get_object_or_404
from rest_framework import generics
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

class PollList(generics.ListCreateAPIView):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PoolSerializer

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PoolSerializer

class ChoiceList(generics.ListCreateAPIView):
    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer

class CreateVote(generics.CreateAPIView):
    serializer_class = serializers.VoteSerializer
