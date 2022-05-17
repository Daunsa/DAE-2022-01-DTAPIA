from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Producto
from .serializers import ProductoSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class ProductosView(APIView):
    
    def get(self,request):
        dataProductos = Producto.objects.all()
        serProductos = ProductoSerializer(dataProductos,many=True)
        return Response(serProductos.data)
    
    def post(self,request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        
        return Response(serProducto.data)
    
class ProductoDetailView(APIView):
    
    def get(self,request,Producto_id):
        dataProducto = Producto.objects.get(pk=Producto_id)
        serProducto = ProductoSerializer(dataProducto)
        return Response(serProducto.data)
    
    def put(self,request,Producto_id):
        dataProducto = Producto.objects.get(pk=Producto_id)
        serProducto = ProductoSerializer(dataProducto,data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)
    
    def delete(self,request,Producto_id):
        dataProducto = Producto.objects.get(pk=Producto_id)
        serProducto = ProductoSerializer(dataProducto)
        dataProducto.delete()
        return Response(serProducto.data)
