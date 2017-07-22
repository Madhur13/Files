from celery import Celery

#from celery.decorators import task
#from celery.task import Task
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

app = Celery('tasks', broker='amqp://localhost//')

@app.task
def SignupTask(self, user):
    subject, from_email, to = 'Welcome', 'refernget@gmail.com', user.email
    html_content = render_to_string('base.html')
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email,[to])
    msg.attach_alternative(html_content, 'text/html')
