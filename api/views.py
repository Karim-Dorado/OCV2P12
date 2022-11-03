from rest_framework import viewsets
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSaleContactOrReadOnly, IsSaleEmployeeOrReadOnly, IsSupportEmployeeOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsSaleEmployeeOrReadOnly]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id',
                        'first_name',
                        'last_name',
                        'email',
                        'phone',
                        'mobile',
                        'company_name',
                        'created_at',
                        'updated_at',
                        'date_revokated']


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsSaleContactOrReadOnly]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id',
                        'client',
                        'sales_contact',
                        'date_signed',
                        'status',
                        'amount',
                        'payement_due',
                        'date_revokated']

    def get_queryset(self):
        return Contract.objects.filter(client=self.kwargs['client_pk'])


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupportEmployeeOrReadOnly]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['id',
                        'name',
                        'contract',
                        'support_contact',
                        'attendees',
                        'start_date',
                        'end_date',
                        'notes',
                        'created_at',
                        'updated_at',
                        'date_revokated']

    def get_queryset(self):
        return Event.objects.filter(contract=self.kwargs['contract_pk'])
