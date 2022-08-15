from django.db import models

# Create your models here.


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        db_table = 'cuenta'


class Movimiento (models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(
        'cuentas.Cuenta', models.DO_NOTHING, db_column='account_id')
    operation_type = models.CharField(max_length=20)
    amount = models.IntegerField()
    changed_at = models.DateTimeField()

    class Meta:
        db_table = 'movimientos'
