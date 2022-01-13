from rest_framework import serializers
from django.contrib.auth import get_user_model
from generic_relations.relations import GenericRelatedField
from rest_framework.validators import UniqueTogetherValidator

from .models import Course, Rating, Text, File, Link, Content


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name')


class CourseEnrollSerializer(CourseSerializer):
    class Meta(CourseSerializer.Meta):
        fields = ('id',)


class ContentSerializer(serializers.ModelSerializer):

    item = GenericRelatedField({
        Text: TextSerializer(),
        Link: LinkSerializer(),
        File: FileSerializer()
    })
    owner = serializers.StringRelatedField

    class Meta:
        model = Content
        fields = ('id', 'item', 'owner')


class RatingSerializer(serializers.ModelSerializer):

    course = serializers.StringRelatedField

    class Meta:
        model = Rating
        exclude = ('reviewer',)
