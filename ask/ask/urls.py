"""ask URL Configuration

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
from django.conf.urls import patterns, include, url


from django.contrib import admin

admin.autodiscover()


from qa import views


urlpatterns = patterns('',

    # Examples:

    # url(r'^$', 'ask.views.home', name='home'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^question/', include('qa.urls')),

    url(r'^$', include('qa.urls')),

    url(r'^login/.*$',views.login_view),

    url(r'^signup/.*$',views.signup),

    url(r'^ask/.*$',views.question_add),

    url(r'^popular/.*$',views.popular),

    url(r'^answer/.*$',views.answer_add),

    url(r'^question/(?P<question_id>[0-9]+)/answer/$', views.answer_add, name='answer_add'),

    url(r'^new/.*$',views.test),

    url(r'^admin/', include(admin.site.urls)),

)
