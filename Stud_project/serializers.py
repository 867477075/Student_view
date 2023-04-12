from rest_framework import serializers

from stud_app.models import Student_Data


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=2)
    roll_no = serializers.IntegerField()

    def create(self, validated_data):
        return Student_Data.objects.create(**validated_data)
