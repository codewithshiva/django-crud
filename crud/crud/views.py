from crud import serialize
from crud.models import MoviesModel
from crud.serialize import MoviesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class MoviesTable(APIView):
    def get(self,request):
        moviesObj=MoviesModel.objects.all()
        moviesSerializeObj=MoviesSerializer(moviesObj,many=True)
        return Response(moviesSerializeObj.data)
    
    def post(self,request):
       serializeobj=MoviesSerializer(data=request.data)
       if serializeobj.is_valid():
           serializeobj.save()
           return Response(200)
       return Response(serializeobj.errors)
   
class UpdateTable(APIView):
    def post(self,request,pk):
        try:
            movieObj=MoviesModel.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        serializeobj=MoviesSerializer(movieObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class DeleteTable(APIView):
    def post(self,request,pk):
        try:
            movieObj=MoviesModel.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        movieObj.delete()
        return Response(200)