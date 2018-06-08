# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from rest_framework import serializers
from controlAsistencia import models

# Create your models here.

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Year
        fields = ('id', 
            'year_number', 
            'division')

class PreceptorSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    email = serializers.ReadOnlyField(source='user.email')
    year = YearSerializer(many=True, read_only=True)
    class Meta:
        model = models.Preceptor
        fields = ('id', 
            'first_name', 
            'last_name', 
            'user', 
            'year', 
            'email',
            'internal_tel')

class StudentSerializer(serializers.ModelSerializer):
    year = YearSerializer(read_only=True)
    class Meta:
        model = models.Student
        fields = ('id', 
            'first_name', 
            'last_name', 
            'dni', 
            'year',
            'student_tag', 
            'list_number', 
            'birthday', 
            'address', 
            'neighbourhood', 
            'city', 
            'status')


class ParentSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    email = serializers.ReadOnlyField(source='user.email')
    childs = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = models.Parent
        fields = ('id',
            'dni', 
            'user', 
            'first_name', 
            'last_name', 
            'email',
            'address',
            'neighbourhood',
            'city',
            'childs')

class RegistroSerializer(serializers.ModelSerializer):
    preceptor = PreceptorSerializer(read_only=True)
    year = YearSerializer(read_only=True)
    class Meta:
        model = models.Registro
        fields = ('id',
            'date',
            'preceptor',
            'year')


class AbsenceSerializer(serializers.ModelSerializer):
    registro = RegistroSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    class Meta:
        model = models.Relation
        fields = ( 'id',
            'origin',
            'justified',
            'registro',
            'percentage',
            'student')
