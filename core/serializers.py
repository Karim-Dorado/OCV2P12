from rest_framework import serializers
from core.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    ModelSerializer that serializes Employee instances.
    """
    class Meta:
        model = Employee
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'department',
            'password',
            ]

    def create(self, validated_data):
        user = Employee.objects.create(username=validated_data["username"],
                                       email=validated_data["email"],
                                       first_name=validated_data["first_name"],
                                       last_name=validated_data["last_name"],
                                       department=validated_data["department"]
                                       )
        user.set_password(validated_data["password"])
        user.save()
        return user
