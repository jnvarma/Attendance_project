from django.contrib import admin
from .models import User,Login,Attendance

#from .models import Login
#from .models import Attendance


# Register your models here.
admin.site.register(User)
admin.site.register(Login)
admin.site.register(Attendance)