from rest_framework import serializers
from rest_framework.serializers import ImageField

from .models import (
    News,
    NewsImage,
    partnerShip,
)


class ImageSerializer(serializers.ModelSerializer):
    image = ImageField(read_only=True)

    class Meta:
        model = NewsImage
        fields = ('id', 'image')


class NewsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "short_desc",
            "full_desc",
            "pub_date",
            "prev_image",
            "image"
        )

    @staticmethod
    def get_image(obj):
        return ImageSerializer(
            NewsImage.objects.filter(article=obj.id),
            many=True
        ).data


class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = partnerShip
        fields = "__all__"
