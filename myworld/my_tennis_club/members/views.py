
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer, TokenPairSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SnippetListSerializer, SnippetDetailSerializer, SnippetCreateUpdateSerializer, TagSerializer
from .models import Snippet, Tag
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import status
from .models import *




class Loginview(APIView):
    def post(self, request):
        def get_tokens_for_login(user):
            
            refresh = RefreshToken.for_user(user)
            print("testtt")
            return {
                'status': "success",
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

        username = request.data.get("username")
        password = request.data.get("password")

        try:
            log =login.objects.filter(username=username, password=password)
            
            user = User.objects.get_or_create(username="user")[0]
            
            token = get_tokens_for_login(user)
            # print("log")
            return Response({'token': token}, status=status.HTTP_200_OK)
            
                
        except:
            return Response({"message": "Wrong Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class SnippetOverviewView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        snippet_count = Snippet.objects.count()
        snippets = Snippet.objects.all()
        serializer = SnippetListSerializer(snippets, many=True)
        return Response({
            'snippet_count': snippet_count,
            'snippets': serializer.data
        })

class SnippetCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = SnippetCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class SnippetDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, snippet_id):
        snippet = Snippet.objects.get(id=snippet_id)
        serializer = SnippetDetailSerializer(snippet)
        return Response(serializer.data)

class SnippetUpdateView(APIView):
    #permission_classes = (IsAuthenticated,)

    def put(self, request, snippet_id):
        snippet = Snippet.objects.get(id=snippet_id)
        serializer = SnippetCreateUpdateSerializer(snippet, data=request.data)
        if serializer.is_valid():
           
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class SnippetDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, snippet_id):
        snippet = Snippet.objects.get(id=snippet_id)
        snippet.delete()
        snippets = Snippet.objects.all()
        serializer = SnippetListSerializer(snippets, many=True)
        return Response(serializer.data)

class TagListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

class TagDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, tag_id):
        snippets = Snippet.objects.filter(tag_id=tag_id)
        serializer = SnippetListSerializer(snippets, many=True)
        return Response(serializer.data)
