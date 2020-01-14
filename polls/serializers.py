from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from . import models

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vote
        fields = ("voted_by","choice", "poll")
        extra_kwargs = {"choice": {"write_only": True},
                        "poll": {"write_only": True}
                        }

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = models.Choice
        fields = ("id","choice_text","votes")

class PoolSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Poll
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data["username"]
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user