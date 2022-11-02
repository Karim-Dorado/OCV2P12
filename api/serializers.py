from rest_framework import serializers
from api.models import Client, Contract, Event
from core.models import Employee


class ClientSerializer(serializers.ModelSerializer):
    """
    ModelSerializer that serializes Client instances.
    """
    sales_contact = serializers.SlugRelatedField(
        queryset=Employee.objects.filter(department = 'sales'),
        slug_field='username',
    )

    class Meta:
        model = Client
        fields = ['id',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'mobile',
                  'company_name',
                  'sales_contact',
                  'created_at',
                  'updated_at',
                  'date_revokated']

    def create(self, validated_data):
        validated_data['sales_contact'] = self.context.get("request", None).user
        self.fields['sales_contact'].readonly = True
        return super().create(validated_data)


class ContractSerializer(serializers.ModelSerializer):
    """
    ModelSerializer that serializes Contract instances.
    """
    sales_contact = serializers.SlugRelatedField(
        queryset=Employee.objects.filter(department = 'sales'),
        slug_field='username',
    )
    class Meta:
        model = Contract
        fields = ['id',
                  'client',
                  'sales_contact',
                  'date_signed',
                  'status',
                  'amount',
                  'payement_due',
                  'date_revokated']
    
    def create(self, validated_data):
        sales_contact = self.context.get("request", None).user
        client = Client.objects.get(pk=self.context.get("view").kwargs["client_pk"])

        contract = Contract.objects.create(
            client = client,
            sales_contact = sales_contact,
            date_signed = validated_data["date_signed"],
            status = validated_data["status"],
            amount = validated_data["amount"],
            payement_due = validated_data["payement_due"],
            date_revokated = validated_data['date_revokated'],
        )
        contract.save()
        return contract


class EventSerializer(serializers.ModelSerializer):
    """
    ModelSerializer that serializes Event instances.
    """
    support_contact = serializers.SlugRelatedField(
        queryset=Employee.objects.filter(department = 'support'),
        slug_field='username',
    )

    class Meta:
        model = Event
        fields = ['id',
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
    
    def create(self, validated_data):
        
        contract = Contract.objects.get(pk=self.context.get("view").kwargs["contract_pk"])

        event = Event.objects.create(
            name = validated_data["name"],
            contract = contract,
            support_contact = validated_data["support_contact"],
            attendees = validated_data["attendees"],
            start_date = validated_data["start_date"],
            end_date = validated_data["end_date"],
            notes = validated_data['notes'],
            date_revokated = validated_data['date_revokated'],
        )
        event.save()
        return event