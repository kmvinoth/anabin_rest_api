from django.urls import path

from anabin.api.views import InstitutionsView

app_name = "anabin"
urlpatterns = [
    path("institutions", view=InstitutionsView.as_view(), name="institutions"),
]
