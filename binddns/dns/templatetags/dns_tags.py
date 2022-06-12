from django import template
from ..models import DNSRECORD

register = template.Library()

@register.simple_tag
def total_dnss():
    return DNSRECORD.created.count()

@register.inclusion_tag('dns/records/most_zones.html')
def most_zones(count=3):
    all_dnss = DNSRECORD.objects.all()
    zone_dict = {}
    zone_list = []
    for dns in all_dnss:
        zoneinfo = dns.zone
        if zone_dict.get(zoneinfo, ""):
            zone_dict[zoneinfo] += 1
        else:
            zone_dict[zoneinfo] = 1
    count_list =  []
    zone_list = zone_dict.keys()
    for key,value in zone_dict.items():
        if value not in count_list:
            count_list.append(value)
    count_list.sort(reverse=True)
    long = len(zone_list)
    final_list = []
    for num in count_list:
        for key,val in zone_dict.items():
            if val == num:
                final_list.append(key)
    if long <= count:
        return {'most_zones': final_list}
    else:
        return {"most_zones": final_list[:count]}







@register.inclusion_tag('dns/records/latest_dnss.html')
def show_latest_dnss(count=3):
    latest_dnss = DNSRECORD.objects.order_by('-created')[:count]
    return {'latest_dnss': latest_dnss}