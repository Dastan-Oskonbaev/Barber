from rest_framework import serializers

from .models import CustomUser, Barber, Profession, District, Language, Portfolio


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'password',
        )

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
        )


class BarberCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Barber
        fields = (
            'id',
            'username',
            'email',
            'password',
        )

    def create(self, validated_data):
        user = Barber.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class BarberSerializer(serializers.ModelSerializer):
    portfolio = PortfolioSerializer(many=True, read_only=True)

    class Meta:
        model = Barber
        fields = (
            'id',
            'username',
            'email',
            'profession',
            'experience',
            'about_me',
            'district',
            'phone_number',
            'work_time_from',
            'work_time_to',
            'work_type',
            'languages',
            'city',
            'photo',
            'portfolio',
        )


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
