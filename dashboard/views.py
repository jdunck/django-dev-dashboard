from __future__ import absolute_import

from django.shortcuts import render
from .models import TracTicketMetric

def index(request):
    metrics = TracTicketMetric.objects.all().order_by('name')
    latest = [m.data.select_related('metric').latest() for m in metrics]
    return render(request, 'dashboard/index.html', {'data': latest})