from django.urls import path
from .views import (InitiativesList, InitiativeDetailView, EventDetailView, StoriesView, 
                    StoryDetailView, EventsView, ContactUsPageView, PrivacyPolicyView, SuccessView,
                    TermsView, HomePageView ,AboutView, CreateInitiative, AddStory, UpdateStory, DeleteInitiative,
                    UpdateInitiative)

app_name = 'tugoingewa'

urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('events/', EventsView.as_view() , name='events'),
    path('addstory/', AddStory.as_view() , name='addstory'),
    path('update_story/<int:pk>/edit/', UpdateStory.as_view() , name='updatestory'),
    path('details/<int:pk>/', StoryDetailView.as_view(), name='details'),
    path('event_details/<int:pk>/', EventDetailView.as_view(), name='event_details'),
    path('stories/', StoriesView.as_view(), name='stories'),
    path('contact/', ContactUsPageView.as_view(), name='contact'),
    path('policy/', PrivacyPolicyView.as_view(), name='policy'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('create_initiative/', CreateInitiative.as_view() , name='create_initiative'),
    path('initiatives/', InitiativesList.as_view(), name='initiatives'),
    path('<slug:slug>/', InitiativeDetailView.as_view(), name='initiative_details'),
    path('<int:pk>/', InitiativeDetailView.as_view(), name='initiative_details'),
    path('initiatives/<int:pk>/Update/', UpdateInitiative.as_view(), name='update_initiative'),
    path('initiatives/<int:pk>/delete/', DeleteInitiative.as_view(), name='delete_initiative'),
]
