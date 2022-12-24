from rest_framework import serializers
from .models import Position, Employee


class PositionSerializer(serializers.Serializer):
    doljnost = serializers.CharField(max_length=30)
    otdel = serializers.CharField(max_length=30)

    def create(self, validated_data):
        position = Position.objects.create(
            doljnost=validated_data['doljnost'],
            otdel=validated_data['otdel'],
        )
        return position

    def update(self, instance, validated_data):
        instance.doljnost = validated_data['doljnost']
        instance.otdel = validated_data['otdel']
        return instance


class EmployeeSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=30)
    birth_date = serializers.DateField()
    position = serializers.IntegerField()
    zarplata = serializers.IntegerField()

    def create(self, validated_data):
        employee = Employee.objects.create(
            fullname=validated_data['fullname'],
            birth_date=validated_data['birth_date'],
            position=validated_data['position'],
            zarplata=validated_data['zarplata'],
        )
        return employee

    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname']
        instance.birth_date = validated_data['birth_date']
        instance.position = validated_data['position']
        instance.zarplata = validated_data['zarplata']
        instance.save()
        return instance
