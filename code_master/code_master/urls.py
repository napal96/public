from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('macro/', include('macro.urls')),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    # path('',lambda req: redirect('/macro/')), #URL Reverse
]
