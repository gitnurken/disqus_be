"""This module contains url configuration.

Include your API resources and views into urlpatterns
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from disqus_be.core_app.api import CommentResource

comment_resource = CommentResource()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(comment_resource.urls)),
)