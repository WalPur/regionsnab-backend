from rest_framework import viewsets


from .models import (
    News,
    NewsImage,
)

from .serializer import (
    NewsSerializer
)


class NewsEndpoint(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all()
