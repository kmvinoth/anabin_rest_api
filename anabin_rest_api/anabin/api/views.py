from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from anabin.models import Institutions
from rest_framework import permissions
from .serializers import InstitutionsSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
# Create your views here.
class InstitutionsView(generics.ListAPIView):

    """
        This class gives you institutions from all the countries

        GET anabin/institutions

        Default

        GET anabin/institutions&limit=20&ordering=id

        Search, filter(by country and status), limit and ordering

        GET anabin/institutions?search='institution_name'&country='country_name',&status='status'&limit=20&ordering=id

    """

    serializer_class = InstitutionsSerializer
    queryset = Institutions.objects.exclude(institution='NA')
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    pagination_class = LimitOffsetPagination
    search_fields = ['institution', 'institution_type']
    filterset_fields = ['country', 'status']
    ordering_fields = ['institution_type', 'status', 'id', 'city_or_place']
    ordering = ['id']