from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Education
from .serializers import EducationSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_tips(request):
    tips = Education.objects.filter(type='tip')
    serializer = EducationSerializer(tips, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_articles(request):
    articles = Education.objects.filter(type='article')
    serializer = EducationSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def add_education(request):
    serializer = EducationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_education(request, pk):
    education = get_object_or_404(Education, pk=pk)
    serializer = EducationSerializer(education, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk)
    education.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
