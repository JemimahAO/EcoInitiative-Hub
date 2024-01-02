from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User
from tugoingewa.models import Initiative

class ProfileView(DetailView):
    http_method_names = ['get']
    model = User
    template_name = 'profiles/user.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Initiative.objects.filter(organiser=user).count
        context['user_posts'] = Initiative.objects.all().filter(organiser=user)
        return context


class UserPostsView(ListView):
    http_method_names = ['get']
    template_name = 'profiles/user_posts.html'
    model = Initiative
    context_object_name = 'initiatives'
    slug_field = 'organiser'
    slug_url_kwarg = 'organiser'
    queryset = Initiative.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['initiatives'] = Initiative.objects.all().order_by('-id')
        return context

class InitiativeDetailView(DetailView):
    http_method_names = ['get']
    model = Initiative
    template_name = "initiatives/initiative_details.html"
    context_object_name = 'initiative'
