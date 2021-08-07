from django.http import response
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
'''
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
'''
from Registro.serializers import ClienteSerializer
from Registro.models import Cliente

# Create your views here.


class ListClienteAPIView(ListAPIView):
    # EndPoint GET Cliente
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class CreateClienteAPIView(CreateAPIView):
    # EndPoint POST Cliente
    query = Cliente.objects.all()

    def get_serializer_class(self):
        return ClienteSerializer


class UpdateClienteAPIview(CreateAPIView):
    # EndPoint PUT Cliente
    serializer_class = ClienteSerializer
    query = Cliente.objects.all()


'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
