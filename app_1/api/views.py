from rest_framework.views import APIView
from rest_framework.response import Response
from app_1.models import Person
from app_1.api.serializers import PersonSerializer
from rest_framework import status

class PersonListAV(APIView):
    def get(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class PersonDetailsAV(APIView):
    def get(self, request, pk):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            return Response({'message':'There is an Error'})

    def delete(self, request, pk):
        person = Person.objects.get(pk=pk)
        person.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'There is no Content'})
