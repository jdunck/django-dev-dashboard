from __future__ import absolute_import, print_function

from django.core.management.base import NoArgsCommand
from ...models import TracTicketMetric

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        verbose = options.get('verbosity', 0)
        for metric in TracTicketMetric.objects.all():
            if verbose:
                if verbose:
                    print("Updating %s ... " % metric.name.lower(), end="")
                datum = metric.data.create(measurement=metric.fetch())
                print(datum.measurement)