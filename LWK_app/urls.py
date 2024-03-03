from django.urls import path
from LWK_app import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('region/',views.region,name="region"),
    path('township/',views.township,name="township")
]
