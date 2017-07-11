import django_filters

from nodeconductor.core import filters as core_filters

from . import models


class ExpertProviderFilter(django_filters.FilterSet):
    customer = core_filters.URLFilter(view_name='customer-detail', name='customer__uuid')
    customer_uuid = django_filters.UUIDFilter(name='customer__uuid')

    class Meta(object):
        model = models.ExpertProvider
        fields = []


class ExpertRequestFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    project = core_filters.URLFilter(view_name='project-detail', name='project__uuid')
    project_uuid = django_filters.UUIDFilter(name='project__uuid')

    class Meta(object):
        model = models.ExpertRequest
        fields = []


class ExpertBidFilter(django_filters.FilterSet):
    expert_request = core_filters.URLFilter(view_name='expert-request-detail', name='expert__uuid')
    expert_request_uuid = django_filters.UUIDFilter(name='expert__uuid')

    class Meta(object):
        model = models.ExpertBid
        fields = []
