from rest_framework import serializers

from api.models import Employee, Student
from drf_day1 import settings


class EmployeeSerializer(serializers.Serializer):
    username = serializers.CharField()
    # password = serializers.CharField()
    # gender = serializers.IntegerField()
    gender = serializers.SerializerMethodField()
    phone = serializers.CharField()
    pic = serializers.SerializerMethodField()

    salt = serializers.SerializerMethodField()

    def get_salt(self, obj):
        return 'salt'

    def get_gender(self, obj):
        # self 是当前序列化器
        # obj是Employee对象

        return obj.get_gender_display()

    def get_pic(self, obj):
        return f'http://127.0.0.1:8000/{settings.MEDIA_URL}{str(obj.pic)}'


class EmployeeDeSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=25,
        min_length=6,
        error_messages={
            "max_length": "长度太长",
            "min_length": "长度太短"
        }
    )
    password = serializers.CharField()
    gender = serializers.SerializerMethodField(required=False)  # required 是否必填

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


class StudentSerializer(serializers.Serializer):
    student_number = serializers.CharField()
    name = serializers.CharField()
    gender = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_photo(self, obj):
        return f'http://127.0.0.1:8000/{settings.MEDIA_URL}{str(obj.photo)}'


class StudentDeSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=20,
        min_length=2,
        error_messages={
            'max_length': '名字太长',
            'min_length': '名字太短',
        }
    )
    password = serializers.CharField(
        max_length=16,
        min_length=6,
        error_messages={
            'max_length': '密码太长',
            'min_length': '密码太短',
        }
    )
    gender = serializers.IntegerField(required=False)
    photo = serializers.ImageField(required=False)
    student_number = serializers.CharField(
        max_length=9,
        min_length=9,
        required=False,
        error_messages={
            'max_length': '学号长度必须是9位数字',
            'min_length': '学号长度必须是9位数字',
        }
    )

    def create(self, validated_data):
        print(validated_data)
        return Student.objects.create(**validated_data)
