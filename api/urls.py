from rest_framework.routers import DefaultRouter

from .views import NewsEndpoint


router = DefaultRouter()

router.register('news', NewsEndpoint, basename='news')

urlpatterns = [
    
] + router.urls
