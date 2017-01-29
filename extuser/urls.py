"""unity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from extuser import views

from django.contrib import admin


urlpatterns = [
    url(r'^$', views.profile, name='profile'),

    #url(r'about/$', views.about, name='about'),
    #url(r'^$', views.user_list, name='users_list'),
    #url(r'^(?P<id>[0-9]+)/$', views.post_detail, name='post-detail'),
    #url(r'^addLike/(?P<id>[0-9]+)/$', views.add_like, name='add-like'),
    url(r'^editProfile', views.edit_profile, name='edit-profile'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
