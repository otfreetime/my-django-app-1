from demo.views import detail
from django.urls import path, include, re_path as url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$',include('demo.urls')),
    # url(r'^blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    # url(r'^admin/', include(admin.site.urls)),
    
]
