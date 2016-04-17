"""bjjapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name='index'),
    url(r'^post/view/(?P<slug>[^\.]+).html$', views.view_post, name='view_blog_post'),
    url(r'^post/categories/(?P<slug>[^\.]+).html$', views.view_category, name='view_category'),
    url(r'^post/subject/(?P<slug>[^\.]+).html$', views.view_type, name='view_type'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
