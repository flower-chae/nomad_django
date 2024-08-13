from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from reviews.serializers import ReviewSerializer
from categories.serializers import CategorySerializer

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = ("name","description",)


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True,many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()


    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self,room):
        print(self.context)
        return room.rating()

    def get_is_owner(self,room):
        request=self.context['request']
        return room.owner == request.user
    # def create(self, validated_data):
    #     print("====csk serializers====")
    #     print(validated_data)
    #     return


class RoomListSerializer(ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()


    class Meta:
        model = Room
        fields = ("pk","name", "country","city","price","rating","is_owner")

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self,room):
        request=self.context['request']
        return room.owner == request.user


