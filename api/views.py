from django.shortcuts import render

# Create your views here.



from rest_framework.views import APIView


from rest_framework.response import Response




class Bookcreatelistview(APIView):


    def get(self,request,*args,**kwargs):


        context={"message":"list book get method"}

        return Response(data=context)
    
    def post(self,request,*args,**kwargs):

        context={"message":"create book post method"}

        return Response(data=context)
    

class BookRetriveUpdateDestroy(APIView):

    def get(self,request,*args,**kwargs):


        context={"message":"retrive book get method"}

        return Response(data=context)
    
    def put(self,request,*args,**kwargs):


        context={"message":"update book put method"}

        return Response(data=context)
    
    
    def delete(self,request,*args,**kwargs):


        context={"message":"remove book delete method"}

        return Response(data=context)
    
    
