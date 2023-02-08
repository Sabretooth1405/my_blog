from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import View_Counter
from .serializers import View_CounterSerializer
@api_view(['GET'])
def view_counterDetail(req,pk):
    view_counter=View_Counter.objects.get(post__id=pk)
    view_counterSerializer=View_CounterSerializer(view_counter)
    return Response(view_counterSerializer.data)

