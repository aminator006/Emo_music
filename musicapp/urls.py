from django.conf.urls import url

from . import views

app_name = 'musicapp'

urlpatterns = [
    url(r"^$", views.SongView.as_view(), name="all_products"),
]
