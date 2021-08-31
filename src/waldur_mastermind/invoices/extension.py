from datetime import timedelta

from waldur_core.core import WaldurExtension


class InvoicesExtension(WaldurExtension):
    class Settings:
        # wiki: https://opennode.atlassian.net/wiki/display/WD/Assembly+plugin+configuration
        WALDUR_INVOICES = {
            'ISSUER_DETAILS': {
                'company': 'University of Tartu',
                'address': 'Ülikooli 18, Tartu',
                'country': 'Estonia',
                'email': '	info@ut.ee',
                'postal': '50090',
                'phone': {'country_code': '372', 'national_number': '7375100',},
                'bank': 'SEB',
                'account': 'EE281010102000234007',
                'vat_code': 'EE100030417',
                'country_code': 'EE',
            },
            # How many days are given to pay for created invoice
            'PAYMENT_INTERVAL': 30,
            'INVOICE_REPORTING': {
                'ENABLE': False,
                'EMAIL': 'accounting@waldur.example.com',
                'CSV_PARAMS': {'delimiter': str(';'),},
                'USE_SAF': False,
                'SERIALIZER_EXTRA_KWARGS': {
                    'start': {'format': '%d.%m.%Y',},
                    'end': {'format': '%d.%m.%Y',},
                },
                'SAF_PARAMS': {'RMAKSULIPP': '20%', 'ARTPROJEKT': 'PROJEKT',},
            },
            'SEND_CUSTOMER_INVOICES': False,
        }

    @staticmethod
    def django_app():
        return 'waldur_mastermind.invoices'

    @staticmethod
    def rest_urls():
        from .urls import register_in

        return register_in

    @staticmethod
    def is_assembly():
        return True

    @staticmethod
    def celery_tasks():
        from celery.schedules import crontab

        return {
            'waldur-create-invoices': {
                'task': 'invoices.create_monthly_invoices',
                'schedule': crontab(minute=0, hour=0, day_of_month='1'),
                'args': (),
            },
            'send-monthly-invoicing-reports-about-customers': {
                'task': 'invoices.send_monthly_invoicing_reports_about_customers',
                'schedule': crontab(minute=0, hour=0, day_of_month='2'),
                'args': (),
            },
            'update-invoices-current-cost': {
                'task': 'invoices.update_invoices_current_cost',
                'schedule': timedelta(hours=24),
                'args': (),
            },
            'send-notifications-about-upcoming-ends': {
                'task': 'invoices.send_notifications_about_upcoming_ends',
                'schedule': timedelta(hours=24),
                'args': (),
            },
        }
