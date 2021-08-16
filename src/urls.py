from django.contrib import admin
from django.urls import path , include
from academic.views import home_page ,show_lectuer ,show_classes
from accounts.views import signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name="home"), 
    
    path('<int:semester_number>',show_classes,name="show_classes"),#128.161/1
    
    
    path('<int:semester_number>/<int:lectuer_number>',show_lectuer,name="show_lectuer"), #128.161/1/1
   
 

    path('signup',signup,name="signup"),
    path('accounts/',include('django.contrib.auth.urls')),

]
