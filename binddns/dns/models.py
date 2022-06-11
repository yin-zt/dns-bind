from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class DNSRECORD(models.Model):
    TYPE_CHOICES = (
        ('A', 'A'),
        ('CNAME', 'CNAME'),
        ('MX', 'MX'),
        ('NS', 'NS'),
        ('PTR', 'PTR')
    )
    target_flag_choice = (
        ('master', "master"),
        ("slave", "slave")
    )
    DNS_STATUS = (
        ('online', 'online'),
        ('offline', 'offline'),
        ('maintain', "maintain")
    )
    id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=128, db_index=True)
    view = models.CharField(max_length=128, blank=True)
    zone = models.CharField(max_length=128, db_index=True)
    type = models.CharField(max_length=128, choices=TYPE_CHOICES, default='A')
    target = models.CharField(max_length=256, null=False)
    target_slave = models.CharField(max_length=256, blank=True)
    target_slave_flag = models.CharField(max_length=128, choices=target_flag_choice, default='master')
    candidates_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apply_dns")
    charge_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="response_dns")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = ('domain', 'zone')

    def __str__(self):
        return self.domain

    def get_absolute_url(self):
        return reverse('dns:dns_detail', args=[self.domain, self.id])
