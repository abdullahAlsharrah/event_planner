from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django.db.models import F
from .models import Event

# from .serializer import CreateSerializer,EventListSerializer,EventDetailsSerilizer
from .serializer import AdvanceEventListSerilizer, EventSerilizer

# Create your views here.
class CreateEvent(CreateAPIView):
    serializer_class = EventSerilizer

class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerilizer

class EventDetails(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerilizer
    lookup_field = 'id'
    lookup_url_kwarg='event_id'

class UpdateEvent(RetrieveAPIView,UpdateAPIView):
    queryset = Event.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg='event_id'
    serializer_class = EventSerilizer

class DeleteEvent(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerilizer
    lookup_field = 'id'
    lookup_url_kwarg='event_id'

class BookedEvent(ListAPIView):
    queryset = Event.objects.all().filter(num_of_seats = F('booked_seats'))
    serializer_class = EventSerilizer

class AdvanceEventList(ListAPIView):
    serializer_class = AdvanceEventListSerilizer

    def get_queryset(self):
        params = self.request.GET
        date = params.get('date')
        if(date):
            events = Event.objects.all().filter(start_date__gte=date).order_by('name')
        else:
            events = Event.objects.all().order_by('name')
        return events
            

class SearchEventByName(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerilizer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('name',)

class Pagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10

class PaginationView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerilizer
    pagination_class=(Pagination)



    