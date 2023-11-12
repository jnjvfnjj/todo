from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined','phone_number')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=100, write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'age', 'phone_number')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        elif attrs['phone_number'][:4] != "+996" or len(attrs['phone_number']) > 13:
            raise serializers.ValidationError({'phone_number':'Неправильный формат номера (+996)'})
        return attrs