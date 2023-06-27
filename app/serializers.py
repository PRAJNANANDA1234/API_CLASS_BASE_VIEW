from rest_framework import serializers
from app.models import *

class ProductSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
