from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name='Home'),
    path('about/',views.about,name='about'),
    path('show/',views.show,name='show'),
    path('department/',views.department,name="department"),
    path('doctors/',views.doctors,name="doctors"),
    path('bookings/',views.bookings,name="bookings")
]