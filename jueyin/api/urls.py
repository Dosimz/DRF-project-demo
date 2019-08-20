from django.urls import re_path
from api.views import course, account, pins

urlpatterns = [
    re_path(r'^course/$', course.CourseView.as_view({'get': 'list'})),
    re_path(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get': 'retrieve'})),
    re_path(r'^auth/$', account.AuthView.as_view()),
    re_path(r'^pins/$', pins.PinsView.as_view())
]