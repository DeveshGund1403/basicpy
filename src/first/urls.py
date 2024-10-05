
from django.contrib import admin
from django.urls import path
from firstapp import views as v1
from secondapp import views as v2


urlpatterns = [
    path('admin/', admin.site.urls),
    path("first-url",v1.firstview),
    path("second-url",v1.secondview),
    path("third-url",v2.thirdview),
    path("fourth-url",v2.fourthview),
]
