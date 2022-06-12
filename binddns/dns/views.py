from django.shortcuts import render, get_object_or_404
from .models import DNSRECORD
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def dns_list(request, ZONE=None):
    zone = "ALL"
    dnss = DNSRECORD.objects.all()
    if ZONE:
        dnss = DNSRECORD.objects.all()
        dnss = dnss.filter(zone=ZONE)
        # dnss = get_object_or_404(DNSRECORD, zone=ZONE)
        zone = ZONE
    paginator = Paginator(dnss, 2)  # 2 dns in each page
    page = request.GET.get('page')
    try:
        dnss = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        dnss = paginator.page(1)
    except EmptyPage:
        # if page is out of range diliver last page of results
        dnss = paginator.page(paginator.num_pages)


    return render(request, 'dns/records/list.html', {'dnss': dnss, 'zone': zone, 'page': page})


def dns_detail(request, domain, id):
    dns = get_object_or_404(DNSRECORD, domain=domain, id=id)
    # dns = DNSRECORD.objects.filter(id__in=ID)
    return render(request, 'dns/records/detail.html', {'dns': dns})