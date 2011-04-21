import datetime
import urllib
import xmlrpclib
from django.conf import settings
from django.contrib.contenttypes.generic import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

class TracTicketMetric(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    query = models.TextField()
    data = GenericRelation('Datum')
    
    def __unicode__(self):
        return self.name
    
    def fetch(self):
        s = xmlrpclib.ServerProxy(settings.TRAC_RPC_URL)
        return len(s.ticket.query(self.query + "&max=0"))
    
    def link(self):
        return "%squery?%s" % (settings.TRAC_URL, self.query)
    
class Datum(models.Model):
    metric = GenericForeignKey()
    content_type = models.ForeignKey(ContentType, related_name='+')
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    measurement = models.BigIntegerField()
    
    class Meta:
        ordering = ['-timestamp']
        get_latest_by = 'timestamp'
        verbose_name_plural = 'data'
        
    def __unicode__(self):
        return "%s at %s: %s" % (self.metric, self.timestamp, self.measurement)