"""
URL configuration for NewProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp.views import home,indax,master,valupass,teacher,froms,storetable,storefrom,storetable2,updatestore,deleteitem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('indax/', indax, name="indax"),
    path('teacher/', teacher, name="teacher"),
    path('master/', master,name="master"),
    path('froms/', froms,name="froms"),
    # path('storetable/', storetable,name="storetable"),
    path('storefrom/', storefrom,name="storefrom"),
    path('storetable2/', storetable2,name="storetable2"),
    path('updatestore/<str:PK>', updatestore,name="updatestore"),
    path('deleteitem/<str:PK>', deleteitem,name="deleteitem"),
    path('valupass/<str:n>', valupass),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)