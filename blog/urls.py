from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog_analysic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/(\w+)/$',views.blog),
    url(r'^btuijian/(\w+)/$',views.btuijian),
    url(r'^paiming/(\w+)/$',views.paiming),
    url(r'^guidang/(\w+)/$',views.guidang),
    url(r'^content/(\w+)/(\w+)/(\w+)/$',views.content),
]
