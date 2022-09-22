from rentalspace import serialize
from rentalspace import serialize
from rentalspace.models import VansModel
from rentalspace.serialize import VansSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class VansTable(APIView):
    def get(self, request):
        vansObj=VansModel.objects.all()
        vnSeralizeObj = VansSerializer(vansObj, many = True)
        return Response(vnSeralizeObj.data)

    def post(self, request):
        serializeObj = VansSerializer(data = request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)