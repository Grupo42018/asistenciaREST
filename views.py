# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status, generics
from . import models as seria
from controlAsistencia import models as contmod

# Create your views here.

class getStudents(generics.ListAPIView):
    serializer_class = seria.StudentSerializer

    def get_queryset(self):
        queryset = contmod.Student.objects.all()
        params = self.request.query_params
        filt = {}
        for i in params.keys():
            a = _check_field(queryset.model, i)
            if a:
                filt[a] = params[i]
        queryset = queryset.filter(**filt)
        return queryset

class getParents(generics.ListAPIView):
    serializer_class = seria.ParentSerializer

    def get_queryset(self):
        queryset = contmod.Parent.objects.all()
        params = self.request.query_params
        filt={}
        print(params)
        for i in params.keys():
            a = _check_field(queryset.model, i)
            if a:
                filt[a] = params[i]
        print filt
        queryset = queryset.filter(**filt)
        return queryset

class getPreceptors(generics.ListAPIView):
    serializer_class = seria.PreceptorSerializer

    def get_queryset(self):
        queryset = contmod.Preceptor.objects.all()
        params = self.request.query_params
        filt = {}
        for i in params.keys():
            a = _check_field(queryset.model, i)
            if a:
                filt[a] = params[i]
        queryset = queryset.filter(**filt)
        return queryset
        
class getYears(generics.ListAPIView):
    serializer_class = seria.YearSerializer

    def get_queryset(self):
        queryset = contmod.Year.objects.all()
        params = self.request.query_params
        filt = {}
        for i in params.keys():
            a = _check_field(queryset.model, i)
            if a:
                filt[a] = params[i]
        queryset = queryset.filter(**filt)
        return queryset
        
class getRegistros(generics.ListAPIView):
    serializer_class = seria.RegistroSerializer

    def get_queryset(self):
        queryset = contmod.Registro.objects.all()
        params = self.request.query_params
        filt = {}
        for i in params.keys():
            a = _check_field(queryset.model, i)
            if a:
                filt[a] = params[i]
        queryset = queryset.filter(**filt)
        return queryset
        
class Absence(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = seria.AbsenceSerializer

    def get_queryset(self):
        queryset = contmod.Relation.objects.all()
        params = self.request.query_params
        filt = {}
        for i in params.keys():
            a = _check_field(queryset.model, i)
            if a:
                filt[a] = params[i]
        queryset = queryset.filter(**filt)
        return queryset
        
class getAbsences(generics.ListCreateAPIView):
    serializer_class = seria.AbsenceSerializer

    def get_queryset(self):
        queryset = contmod.Relation.objects.all()
        params = self.request.query_params
        filt = {}
        for i in params.keys():
            a = _check_field(queryset.model, i)
            if a:
                filt[a] = params[i]
        queryset = queryset.filter(**filt)
        return queryset
        
def check(request):
    res = HttpResponse()
    res['Allow'] = 'HEAD'
    if request.method != 'HEAD':
        res.status_code = 400
    return res


def _check_field(model, filters):
    last = model.objects.first()
    fields = filters.split('__')
    for field in fields:
        try:
            last=getattr(last, field)
        except AttributeError as e:
            return False

    return filters