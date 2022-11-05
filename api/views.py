from rest_framework import viewsets
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import (
                          IsSalesContactOrReadOnly,
                          IsContractSalesContactOrReadOnly,
                          IsSupportContactOrReadOnly,
                          IsEventCommmingOrReadOnly)
from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsSalesContactOrReadOnly]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['first_name',
                        'last_name',
                        'email']


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsContractSalesContactOrReadOnly]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['client',
                        'date_signed',
                        'amount']

    def get_queryset(self):
        return Contract.objects.filter(client=self.kwargs['client_pk'])


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupportContactOrReadOnly, IsEventCommmingOrReadOnly]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['name',
                        'start_date',
                        'end_date']

    def get_queryset(self):
        return Event.objects.filter(contract=self.kwargs['contract_pk'])
