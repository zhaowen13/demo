# -*- coding: utf-8 -*-
from .models import case
# from django.contrib.auth.models import User
from rest_framework import viewsets, filters, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CaseSerializer,UserSerializer
from django.http.response import JsonResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class CaseViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = case.objects.all()
    serializer_class = CaseSerializer
    filter_backends = (DjangoFilterBackend,)
    # search_fields = ('name','fundcode')
    filter_fields = ('name',)

    def create(self, request):
        serializer = CaseSerializer(data=request.data['from'])
        # list_data = OptionalfundSerializer(queryset, many=True, context={'request': request})
        if case.objects.filter(name=request.data['from']['name']).exists():
            raise Http404
        else:
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "添加成功"})

class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


