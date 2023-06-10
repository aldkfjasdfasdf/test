from django.conf.urls import url

from .views import (
    create_email,
    tracking_pixel_view
)


urlpatterns = [
    url(r'^tracking/(?P<tracking_pixel_id>\d+)/$', tracking_pixel_view, name='tracking_pixel_view'),
    url('', create_email, name='create_email'),
]
