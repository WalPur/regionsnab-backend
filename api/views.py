from rest_framework import viewsets


from .models import (
    News,
    NewsImage,
)

from .serializer import (
    NewsSerializer,
    PartnershipSerializer
)


class NewsEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all().order_by('-pub_date')

class PartnerShipEndpoint(viewsets.ModelViewSet):
    http_method_names = ['post']
    serializer_class = PartnershipSerializer
