from django.conf.urls import url
from django.urls import path

from registration import views as v
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registration/", v.registration, name="registration"),
    path("create/", views.create, name="index"),
    path("staff/", views.staff, name="staff"),
    path("invite/", views.invite, name="invite"),
    path("logout/", views.logout_now, name="logout_now"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        v.activate_account, name='activate'),
]
