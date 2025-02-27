from django.http import JsonResponse, HttpResponse
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class PingApiView(APIView):
    def get(self, request):
        return Response({"result": "pong"})

class Challenge1APIView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Items(type=openapi.TYPE_INTEGER),
    ))
    def post(self, request):
        array = request.data

        # Write the code for Challenge 1 here

        return Response(-1)

class Challenge2APIView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Items(type=openapi.TYPE_INTEGER),
    ))
    def post(self, request):
        array = request.data

        # Write the code for Challenge 2 here

        return Response([])

class Challenge3APIView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'order': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ))
    def post(self, request):
        order = request.data['order']

        # Write the code for Challenge 3 here

        return Response("")
