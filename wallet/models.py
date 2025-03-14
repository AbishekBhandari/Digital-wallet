from django.db import models
from django.contrib.auth.models import User
import pytz
import nepali_datetime
from django.db import models
from django.utils.timezone import localtime

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Transaction(models.Model):
    wallet = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('Credit', 'Credit'), ('Debit', 'Debit')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_nepali_time(self):
        # Convert to Nepali Standard Time (UTC+5:45)
        nst_timezone = pytz.timezone("Asia/Kathmandu")
        local_time = localtime(self.timestamp, nst_timezone)

        # Convert date & time separately
        nepali_date = nepali_datetime.date.from_datetime_date(local_time.date())  # Convert date
        nepali_time = local_time.strftime("%H:%M:%S")  # Keep time as it is
        
        return f"{nepali_date} {nepali_time}"