"""events_plannner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from events.views import AdvanceEventList, BookedEvent, CreateEvent, DeleteEvent, EventDetails, EventList, PaginationView, SearchEventByName, UpdateEvent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/create', CreateEvent.as_view()),
    path('events/', EventList.as_view()),
    path('events/advance', AdvanceEventList.as_view()),
    path('events/filter', SearchEventByName.as_view()),
    path('events/pagination', PaginationView.as_view()),
    path('events/<int:event_id>/', EventDetails.as_view()),
    path('events/update/<int:event_id>/', UpdateEvent.as_view()),
    path('events/delete/<int:event_id>/', DeleteEvent.as_view()),
    path('events/fully-booked/', BookedEvent.as_view()),
]
