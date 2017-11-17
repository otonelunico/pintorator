from django.conf.urls import url
from .views import Login, Logout, Calculo

# Normal Url
urlpatterns = [
    url(r'^$', Login.as_view(), name='login'),
    url(r'^calculo', Calculo.as_view(), name='pintura'),
]