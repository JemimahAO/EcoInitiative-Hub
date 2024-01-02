from typing import Any
from django import http
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, FormView, ListView
from .models import Event
from .forms import AddEventForm
from django.contrib import messages


class IndexPageView(ListView):
    http_method_names = ['get']
    template_name = "index.html"
    model = Event
    context_object_name = 'events'
    queryset = Event.objects.all().order_by('-id')[0:10]

# class HomePageView(ListView):
#     http_method_names = ['get']
#     template_name = 'home.html'
#     model = Event
#     context_object_name = 'events'
#     queryset = Event.objects.all().order_by('-id')[0:4]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['events'] = Event.objects.all().order_by('-id')[0:4]
    #     return context
       

class EventDetailView(DetailView):
    model = Event
    template_name = "event_details.html"
    

class AddEventView(FormView):
    form_class = AddEventForm
    template_name = "add_event.html"
    success_url = "/"

    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # create a new form

        new_object = Event.objects.create(
            title = form.cleaned_data['title'],
            event_image = form.cleaned_data['event_image'],
            event_date = form.cleaned_data['event_date'],
            start_time = form.cleaned_data['start_time'],
            end_time = form.cleaned_data['end_time'],
            price = form.cleaned_data['price'],
            location = form.cleaned_data['location'],
            description = form.cleaned_data['description'],
        )
        
        messages.add_message(self.request, messages.SUCCESS, 'Your Event Has Been Successfully Created')
        return super().form_valid(form)
    

class ContactUsPageView(TemplateView):
    template_name = "contact_us.html"

