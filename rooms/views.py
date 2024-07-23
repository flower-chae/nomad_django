# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Room

# # Create your views here.
# def see_all_rooms(request):
#     rooms = Room.objects.all()
#     # return HttpResponse("see all rooms!")
#     return render(request,"all_rooms.html", {'rooms': rooms, 'title':"Hello! this title comes from django!"})

# def see_one_room(request, room_pk):
#     try:
#         room = Room.objects.get(pk=room_pk)
#         # return HttpResponse(f"see room with id: {room_id}")
#         return render(request, "room_detail.html", {'room':room}) 
#     except Room.DoesNotExist:
#         return render(request, "room_detail.html", { 'not_found' : True})


from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Amenity
from .serializers import AmenitySerializer

class Amenities(APIView):

    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = AmenitySerializer(data=request.data) #객체는 없고 데이터만 있음 create
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        print("==csk1===")
        print(type(amenity))
        print(amenity)
        serializer = AmenitySerializer(amenity)
        print(serializer)
        print("===csk2===")
        print(type(serializer.data))
        print(serializer.data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity,data=request.data,partial=True) #객체와 데이터주어져야 update
        if serializer.is_valid():
            updated_amenity=serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)
