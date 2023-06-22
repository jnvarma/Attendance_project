#from django.contrib import admin
from django.urls import path
#from . import views
from .views import register,login_page,attendance,logout
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     #path('admin/', admin.site.urls),
     
     path("",register,name="register"),
     path("login_page/",login_page,name="login_page"),
     path("attendance/",attendance,name="attendance"),
     path("logout/",logout, name="logout"), 
     
]




    
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)