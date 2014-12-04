from django.conf.urls import patterns, include, url
from django.contrib import admin
from teams.views import OrganizationListView, OrganizationDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'league.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', OrganizationListView.as_view(), name='organization-list'),
    url(r'^(?P<slug>[-_\w]+)/$', OrganizationDetailView.as_view(), name='organization-detail'),
)
