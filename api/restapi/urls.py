from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from restapi import views


urlpatterns = patterns('',
    url(r'^api$', views.NameList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$',views.NameDetail.as_view()),
)





#still cant figure out whats wrong with urlpatterns


#problem found --> I am using urlsuffix patterns in restapi/urls.py as well as api/urls.py
#ie in both project and app use it in one place only . Done!!


#urlpatterns = format_suffix_patterns(urlpatterns)