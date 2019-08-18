from django.urls import path

from . views import IndexView

app_name = 'account'


urlpatterns = [
    path('account/', IndexView.as_view(), name='index'),
]
