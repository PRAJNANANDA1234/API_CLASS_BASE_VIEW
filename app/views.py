from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class productCrud(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PQS=Product.objects.get(id=id)

        PJSD=ProductSerilizers(PQS)
        return Response(PJSD.data)
    
    def post(self,request,id):
       PMSD=ProductSerilizers(data=request.data)
       if PMSD.is_valid():
          SPO=PMSD.save()
          return  Response({'message':'Product is created'})
       return Response({'Failed':'Product is not created'})
    def put(self,request,id):
       id=request.data['id']
       PO=Product.objects.get(id=id)
       UPO=ProductSerilizers(PO,data=request.data)
       if UPO.is_valid():
          UPO.save()
          return  Response({'message':'Product is update'})
       return Response({'Failed':'Product is not update'})
    def patch(self,request,id):
       id=request.data['id']
       PO=Product.objects.get(id=id)
       PO.Pname=request.data['Pname']
       PO.save()
       return Response({'Success':'Product is Partially update'})
    def delete(self,request,id):
       Product.objects.get(id=id).delete()
       return Response({'Success':'Product is deleted'})
       
    
    