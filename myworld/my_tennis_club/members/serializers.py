from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import Tag, Snippet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TokenPairSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        return RefreshToken(validated_data['refresh'])


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')

class SnippetListSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True)

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'timestamp', 'tag')

class SnippetDetailSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True)

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'content', 'timestamp', 'tag')

class SnippetCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'
