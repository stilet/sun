from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^homes', views.HomeListView.as_view(), name='homes_list'),  # список участков
]
