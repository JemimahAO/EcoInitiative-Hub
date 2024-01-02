from django.urls import path
from .views import ProfileView, UserPostsView, InitiativeDetailView

app_name = 'profiles'

urlpatterns = [
       
        path('user_posts/<str:username>', UserPostsView.as_view(), name='user_posts'),
        path('<int:pk>/', InitiativeDetailView.as_view(), name='initiative_details'),

        path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
]
