from typing import Any
from django import http
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, FormView, ListView, UpdateView, CreateView, DeleteView
from .models import Event, Story, Initiative, Contact
from .forms import AddEventForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.utils.text import slugify
from django.conf import settings
from django.http import JsonResponse
from .forms import AddInitiativeForm
from django.conf import settings
from django.core.mail import send_mail


class EventsView(ListView):
    http_method_names = ['get']
    template_name = 'events.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all().order_by('-id')
        context['recommended'] = Story.objects.all().order_by('id')[0:4]
        return context
    

class HomePageView(TemplateView):
    http_method_names = ['get']
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories'] = Story.objects.all().order_by('-id')[0:5]
        context['projects'] = Initiative.objects.all().order_by('-id')[0:3]
        context['events'] = Event.objects.all().order_by('-id')[0:5]
        return context


class EventDetailView(DetailView):
    http_method_names = ['get']
    model = Event
    context_object_name = 'event'
    template_name = "event_details.html"


class ContactUsPageView(TemplateView):
    template_name = "contact_us.html"

class PrivacyPolicyView(TemplateView):
    template_name = "privacy_policy.html"

class TermsView(TemplateView):
    template_name = "terms.html"

class SuccessView(TemplateView):
    template_name = "initiatives/initiatives.html"

class success(TemplateView):
    template_name = "success/success.html"

class AboutView(TemplateView):
    template_name = "about.html"


class StoriesView(ListView):
    http_method_names = ['get']
    template_name = 'stories.html'
    model = Story

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories'] = Story.objects.all().order_by('-id')
        context['recommended'] = Story.objects.all().order_by('id')[0:4]
        return context

class ArticlesView(ListView):
    template_name = 'Include/articles.html'
    model = Story
    context_object_name = 'stories'
    ordering = ['-date_posted']
    paginate_by = 4


class DeleteEventView(DeleteView):
    model = Event
    template_name = "delete_event.html"
    success_url = reverse_lazy('events')


#Initiatives

class InitiativesList(ListView):
    template_name = 'initiatives/initiatives.html'
    model = Initiative
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['initiatives'] = Initiative.objects.filter(status=1).order_by('-date_created')
        return context

class InitiativeDetailView(DetailView):
    http_method_names = ['get']
    model = Initiative
    template_name = "initiatives/initiative_details.html"
    context_object_name = 'initiative'

class CreateInitiative(CreateView):
    model = Initiative
    template_name = 'initiatives/create_initiative.html'
    fields = ['title', 'initiative_image', 'description', 'start_date', 'end_date', 'goals', 'status']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.organiser = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()

        messages.success(self.request, 'Your Initiative Has been Created Successfully')
        
        # Use the 'redirect' function to go to a specific URL
        return redirect('tugoingewa:initiatives')


class UpdateInitiative(UpdateView):
    model = Initiative
    template_name = 'initiatives/update_initiative.html'
    fields = ['title', 'initiative_image', 'description', 'start_date', 'end_date', 'goals']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update
        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your Initiative Has been Updated Successfully'
        )
        return reverse_lazy('initiatives')
    
    def get_queryset(self):
        return self.model.objects.filter(organiser=self.request.user)

class DeleteInitiative(DeleteView):
    model = Initiative
    template_name = 'initiatives/delete_initiative.html'

    def get_success_url(self):
        messages.success(
            self.request, 'Your Initiative Has been Deleted'
        )
        return reverse_lazy('initiatives')
    
    def get_queryset(self):
        return self.model.objects.filter(organiser=self.request.user)


#Stories

class AddStory(CreateView):
    model = Story
    template_name = 'addstory.html'
    fields = '__all__'
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()

        messages.success(self.request, 'Your Story Has been Created Successfully')
        
        # Use the 'redirect' function to go to a specific URL
        return redirect('tugoingewa:stories')
    
class UpdateStory(UpdateView):
    model = Story
    template_name = 'updatestory.html'
    fields = '__all__'
    success_url = reverse_lazy('stories')

class StoryDetailView(DetailView):
    http_method_names = ['get']
    model = Story
    context_object_name = 'story'
    template_name = "story_details.html"


# contact us
class ContactForm(FormView):
    model = Contact
    fields = '__all__'
    def contact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                subject = 'welcome to Eco Initiative Hub'
                message = "Our team will gt back to you within 24 hours."
                email_from = settings.EMAIL_HOST_USER
                email = form.cleaned_data['email'] 
                recipient_list = email
                send_mail(subject, message, email_from, [recipient_list])
                return render(request, 'success.html')
            form = ContactForm()
            context = {'form': form}
            return render(request, 'contact_us.html', context)
