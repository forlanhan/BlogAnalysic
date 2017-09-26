from django.conf.urls import include, url
from django.contrib import admin
from login import views

urlpatterns = {
    # Examples:
    # url(r'^$', 'blog_analysic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', views.login),
    url(r'^antion/$', views.antion)
}
