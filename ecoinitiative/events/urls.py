from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from tugoingewa import urls as tugoingewa_urls
from profiles import urls as profiles_urls
#from initiatives import urls as initiatives_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(tugoingewa_urls, namespace='tugoingewa')),
    path('', include(profiles_urls, namespace='profiles')),
    #path('', include(initiatives_urls, namespace='initiatives')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
