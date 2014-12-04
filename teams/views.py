from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from teams.models import Organization, League

class OrganizationListView(ListView):

    model = Organization

    def get_context_data(self, **kwargs):
        context = super(OrganizationListView, self).get_context_data(**kwargs)
        return context

class OrganizationDetailView(DetailView):
    model = Organization

    def get_context_data(self, **kwargs):
        context = super(OrganizationDetailView, self).get_context_data(**kwargs)
        context['leagues'] = League.objects.all
        return context