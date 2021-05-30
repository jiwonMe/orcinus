from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LetterSerializer


class LetterView(APIView):
    def post(self, request):
        letter_serializer = LetterSerializer(data=request.data)

        if letter_serializer.is_valid():

            letter_serializer.save()

            return Response(letter_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(letter_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SailorView(APIView):
    def post(self, request):
        print(request.data['mobileco'])
        return Response(request.data, status=status.HTTP_201_CREATED)
