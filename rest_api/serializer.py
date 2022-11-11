from rest_framework import serializers, validators
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('password','user_name', 'user_id')

        extra_kwargs = {
            "nickname": {
                "validators":[
                    validators.UniqueValidator(
                        User.objects.all(),
                        "이미 존재하는 유저명입니다."
                    )
                ]
            },
            "password": {"write_only":True} #write_only를 통해 GET요청 시 접근을 차단
        }

    def create(self, validated_data):
        print(validated_data)
        password = validated_data['password']
        user_id = validated_data['user_id']
        user_name = validated_data['user_name']
        user = User.objects.create_user(
            user_id=user_id,
            user_name=user_name,
            password=password,
        )
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'user_id')