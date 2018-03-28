from __future__ import unicode_literals

from . import utils


def format_event(tags):
    return {
        'measurement': 'events',
        'tags': tags,
        # fields is required, but empty
        'fields': {
            'value': 0
        }
    }


def log_resource_created(sender, instance, **kwargs):
    client = utils.get_influxdb_client()
    if not client:
        return
    title = 'Resource {resource_name} has been created.'.format(resource_name=instance.full_name)
    point = format_event({
        'title': title,
        'type': 'resource_created',
    })
    utils.write_points(client, [point])


def log_resource_deleted(sender, instance, **kwargs):
    client = utils.get_influxdb_client()
    if not client:
        return
    title = 'Resource {resource_name} has been deleted.'.format(resource_name=instance.full_name)
    point = format_event({
        'title': title,
        'type': 'resource_deleted',
    })
    utils.write_points(client, [point])
