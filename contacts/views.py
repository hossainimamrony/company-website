from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework import generics,mixins
from emails import email_send
from emails.serializers import EmailModelSerializer
import json
from emails.models import EmailModel


class ConactUs(APIView):

    def post(self,request):
        serializer=ContactSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            
            fn=serializer.data['Full_Name']
            #ln=serializer.data['Last_Name']
            mb=serializer.data['Mobile']
            em=serializer.data['Email']
            pp=serializer.data['Purpose']
            ms=serializer.data['Message']

            sub="New Contacts"
            b= "Full_Name:  "+fn+"\n\n"+"Mobile:  "+mb+"\n\n"+"Email:  "+em+"\n\n"+"Purpose:  "+pp+"\n\n"+"Message:  "+ms+"\n\n"
            x=serializer.data['Email']
            to=[x,'team.techelementbd@gmail.com']
            email_send.send(sub,b,to)
            s=EmailModel()
            s.email=x
            s.save()
            
            return Response({"Message":"Successfully Sended Contact information !"})
        
        return Response({"Message":"Error"})
    

    

