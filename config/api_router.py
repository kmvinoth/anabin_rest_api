from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from anabin_rest_api.users.api.views import UserViewSet
from anabin_rest_api.anabin.api.views import InstitutionsViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("anabin/institutions", InstitutionsViewSet)


app_name = "api"
urlpatterns = router.urls
