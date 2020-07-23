from django.urls import path

from anabin.api.views import InstitutionsViewSet

app_name = "anabin"
urlpatterns = [
    path("institutions", view=InstitutionsViewSet.as_view({'get': 'list'}), name="institutions"),
]
