from rest_framework import serializers
from blog.models import View_Counter

class View_CounterSerializer(serializers.ModelSerializer):

    class Meta:
        model=View_Counter
        fields="__all__"
        read_only_fields = ('post',)
