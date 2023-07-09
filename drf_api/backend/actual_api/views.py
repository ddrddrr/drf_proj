from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from products.serializers import FullProductSerializer


@api_view(["POST"])
def api_home(request):
    book_data = request.data
    # product = Product.objects.all().get(id=2)
    if book_data:
        serialized_book = FullProductSerializer(data=book_data)
        if serialized_book.is_valid(raise_exception=True):
            # instance = serialized_book.save()
            print(serialized_book.data)
            return Response(serialized_book.data)

    return Response({"no_data": "no data has been recieved"}, status=404)
