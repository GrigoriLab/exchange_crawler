from django.urls import include, path
from apps.api.v1.quote import QuoteView
from rest_framework.authtoken.views import obtain_auth_token

apipatterns = [
    path("quotes/", QuoteView.as_view(), name='quotes'),
    path('auth/', obtain_auth_token, name='auth'),
]


urlpatterns = [
    path("v1/", include(apipatterns)),
]
