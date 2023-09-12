from rest_framework import serializers

from .models import Category, Blog, Description


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = (
            'id',
            'category',
            'date',
            'name',
            'image',
            'description',
        )


class CategorySerializer(serializers.ModelSerializer):
    blog = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'blog',
        )
