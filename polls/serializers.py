from rest_framework import serializers

from . import models

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vote
        fields = "__all__"

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = models.Choice
        fields = "__all__"

class PoolSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = models.Poll
        fields = "__all__"