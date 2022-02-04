from django.urls import include, path
from apps.api.v1.quote import QuoteView

apipatterns = [
    path("quotes/", QuoteView.as_view(), name='quotes'),
]


urlpatterns = [
    path("v1/", include(apipatterns)),
]
