from django.utils import timezone
from rest_framework import serializers
from .models import Task, SubTask, Category
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['title', 'description', 'status', 'deadline']
        fields = '__all__'


class SubTaskCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SubTask
        # fields = ['title', 'description', 'task', 'status', 'deadline', 'created_at']
        fields = ['id', 'owner', 'task', 'title', 'description', 'status', 'deadline', 'created_at']


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return value

    def create(self, validated_data):
        name = validated_data.get('name')
        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name', instance.name)
        if Category.objects.filter(name=name).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError("Category with this name already exists.")
        instance.name = name
        instance.save()
        return instance


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['title', 'description', 'status', 'deadline', 'created_at']


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline', 'created_at', 'subtasks']


class TaskCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['title', 'owner', 'description', 'status', 'deadline']

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("The deadline cannot be in the past.")
        return value


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user
