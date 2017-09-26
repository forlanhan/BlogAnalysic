from django.conf.urls import include, url
from django.contrib import admin
from index import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_analysic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$',views.index),
    url(r'^user/(\w+)/$',views.user),
    url(r'^focus/(\w+)/$',views.focus),
    url(r'^fans/(\w+)/$',views.fans),
    url(r'^tuijian/(\w+)/$',views.tuijian),
]
