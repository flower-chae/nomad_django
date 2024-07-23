# from django.http import JsonResponse
# from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Category
from .serializers import CategorySerializer



@api_view(["GET", "POST"])
def categories(request):

    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
        # return Response(
        #     {
        #         "ok": True,
        #         "categories" :serializer.data,
        #     }
        # )


        # all_categories = Category.objects.all()

        # return JsonResponse({
        #         "ok": True,
        #         "categories" : serializers.serialize("json",all_categories),
            
        #     })
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            print("==csk==")
            print(type(new_category))
            print(new_category)
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def category(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
            raise NotFound
    
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data, partial=True,)
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)


# {
#     "name": "Category from DRF",
#     "kind": "rooms"
# }