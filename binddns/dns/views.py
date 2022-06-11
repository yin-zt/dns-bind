from django.shortcuts import render, get_object_or_404
from .models import DNSRECORD

def dns_list(request, ZONE=None):
    zone = "ALL"
    dnss = DNSRECORD.objects.all()
    if ZONE:
        dnss = DNSRECORD.objects.all()
        dnss = dnss.filter(zone=ZONE)
        # dnss = get_object_or_404(DNSRECORD, zone=ZONE)
        zone = ZONE

    return render(request, 'dns/records/list.html', {'dnss': dnss, 'zone': zone})


def dns_detail(request, domain, id):
    dns = get_object_or_404(DNSRECORD, domain=domain, id=id)
    # dns = DNSRECORD.objects.filter(id__in=ID)
    return render(request, 'dns/records/detail.html', {'dns': dns})