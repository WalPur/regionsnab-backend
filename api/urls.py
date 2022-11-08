from rest_framework.routers import DefaultRouter

from .views import NewsEndpoint, PartnerShipEndpoint


router = DefaultRouter()

router.register('news', NewsEndpoint, basename='news')
router.register('partner', PartnerShipEndpoint, basename='partner')

urlpatterns = [
    
] + router.urls
