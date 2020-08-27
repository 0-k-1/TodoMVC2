
# from django.urls import path
from django.conf.urls import url
from App.views import todoMVC_view,save_view

urlpatterns = [
    url('', todoMVC_view),
    url(r'^save/', save_view, name='save')
]
