from rest_framework import serializers
from api.models import Client, Contract, Event
from core.models import Employee
from core.serializers import EmployeeSerializer


class ClientSerializer(serializers.ModelSerializer):
    """
    ModelSerializer that serializes Client instances.
    """
    sales_contact = EmployeeSerializer(read_only=True)

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
                  'is_prospect',
                  'created_at',
                  'updated_at',
                  'date_revokated']
    
    def create(self, validated_data):
        sales_contact = self.context.get("request", None).user

        client = Client.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data['email'],
            phone=validated_data['phone'],
            mobile=validated_data['mobile'],
            company_name=validated_data['company_name'],
            sales_contact=sales_contact,
            is_prospect=validated_data['is_prospect'],
            date_revokated=validated_data['date_revokated'],
        )
        client.save()
        return client


class ContractSerializer(serializers.ModelSerializer):
    """
    ModelSerializer that serializes Contract instances.
    """
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = ['id',
                  'client',
                  'date_signed',
                  'status',
                  'amount',
                  'payement_due',
                  'date_revokated']

    def create(self, validated_data):
        client = Client.objects.get(pk=self.context.get("view").kwargs["client_pk"])
        if client.is_prospect == True:
            raise serializers.ValidationError("You can't create a contract to a client who is still a prospect")
        else:
            contract = Contract.objects.create(
                client=client,
                date_signed=validated_data["date_signed"],
                status=validated_data["status"],
                amount=validated_data["amount"],
                payement_due=validated_data["payement_due"],
                date_revokated=validated_data['date_revokated'],
                )
            contract.save()
            return contract


class EventSerializer(serializers.ModelSerializer):
    """
    ModelSerializer that serializes Event instances.
    """
    contract = ContractSerializer(read_only=True)
    support_contact = serializers.SlugRelatedField(
        queryset=Employee.objects.filter(department='support'),
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
        if contract.status == False:
            raise serializers.ValidationError("You can't create an event while a contract is still not signed")
        else:
            event = Event.objects.create(
                name=validated_data["name"],
                contract=contract,
                support_contact=validated_data["support_contact"],
                attendees=validated_data["attendees"],
                start_date=validated_data["start_date"],
                end_date=validated_data["end_date"],
                notes=validated_data['notes'],
                date_revokated=validated_data['date_revokated'],
            )
            event.save()
            return event
