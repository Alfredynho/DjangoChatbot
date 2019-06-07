from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.conf import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^messenger/', include(('apps.messenger.urls','messenger'),namespace='messenger')),    
    path('', include(('apps.author.urls','author'),namespace='author')),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
