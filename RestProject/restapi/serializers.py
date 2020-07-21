from rest_framework import serializers
from .models import Occurrence
from datetime import datetime
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    occurrences = serializers.PrimaryKeyRelatedField(many=True, queryset=Occurrence.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'occurrences']


# class: CreateOccurrenceSerializer
# Serializer usado na criacao de uma ocorrencia

class CreateOccurrenceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=100, required=True)
    lat = serializers.FloatField(required=True)
    lon = serializers.FloatField(required=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.ChoiceField(choices=['CONSTRUCTION', 'SPECIAL_EVENT', 'INCIDENT', 'WEATHER_CONDITION',
                                                'ROAD_CONDITION'])

    def create(self, validated_data):
        return Occurrence.objects.create(**validated_data)


# class EditOccurrenceSerializer
# Serializer usado na edicao de uma ocorrencia

class EditOccurrenceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(read_only=True)
    lat = serializers.FloatField(read_only=True)
    lon = serializers.FloatField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    state = serializers.ChoiceField(choices=['por validar', 'validado', 'resolvido'])
    category = serializers.ChoiceField(choices=['CONSTRUCTION', 'SPECIAL_EVENT', 'INCIDENT', 'WEATHER_CONDITION',
                                                'ROAD_CONDITION'], read_only=True)

    def update(self, instance, validated_data):
        instance.edit_date = validated_data.get('edit_date', datetime.now())
        instance.state = validated_data.get('state', instance.state)
        instance.category = validated_data.get('category', instance.category)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.save()
        return instance


# class OccurrenceSerializer
# Serializer usado na listagem de todas as ocorrencias

class OccurrenceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=100)
    lat = serializers.FloatField(required=True)
    lon = serializers.FloatField(required=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    initial_date = serializers.DateTimeField()
    edit_date = serializers.DateTimeField()
    state = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Occurrence.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.initial_date = validated_data.get('initial_date', instance.initial_date)
        instance.edit_date = validated_data.get('edit_date', instance.edit_date)
        instance.state = validated_data.get('state', instance.state)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
