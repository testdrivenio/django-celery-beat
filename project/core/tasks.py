from celery import shared_task
from django.core.management import call_command


@shared_task
def sample_task():
    print("The sample task just ran.")


@shared_task
def send_email_report():
    call_command("email_report", )
