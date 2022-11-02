from django.db import models
from core.models import Employee, TimeStamped


class Client(TimeStamped):
    """
    Model that represents a Client.
    """
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=20, unique=True)
    company_name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Contract(TimeStamped):
    """
    Model that represents a Contract.
    """
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(to=Employee, on_delete=models.CASCADE, default="")
    date_signed = models.DateTimeField()
    status = models.BooleanField(default=False)
    amount = models.FloatField(null=True)
    payement_due = models.DateTimeField()

    def __str__(self):
        return f'Contract n°: {self.pk}, client: {self.client}'


class Event(TimeStamped):
    """
    Model that represents a Event.
    """
    name = models.CharField(max_length=100)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(to=Employee,
                                        on_delete=models.CASCADE,
                                        related_name='events')
    attendees = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    notes = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name}'
