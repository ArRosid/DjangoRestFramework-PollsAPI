from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from . import models
from . import serializers

class PollList(APIView):
    def get(self, request):
        pools = models.Poll.objects.all()[:20]
        data = serializers.PoolSerializer(pools, many=True).data
        return Response(data)

class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(models.Poll, pk=pk)
        data = serializers.PoolSerializer(poll).data
        return Response(data)