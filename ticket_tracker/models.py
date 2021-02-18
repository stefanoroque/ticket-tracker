from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    role = models.CharField(max_length=32)

class Project(models.Model):
    # The name of the project
    name = models.CharField(max_length=32, unique=True)
    # Short description of the project
    description = models.TextField()
    # Users who are assigned to this project
    assigned_users = models.ManyToManyField(User, related_name="users")


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed')
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]

    # Project that this ticket is for
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # Short summery of the issue
    summary = models.CharField(max_length=255)
    # More detailed description of the issue
    description = models.TextField()
    # The user who submitted the ticket
    submitter =  models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="submitter")
    # The developer that this ticket is assigned to
    assigned_developer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="dev")
    # The status of this ticket
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default='Open',
    )
    # The priority of this ticket
    priority = models.CharField(
        max_length=16,
        choices=PRIORITY_CHOICES,
        default='Low',
    )
    # The date the ticket was created
    created_on = models.DateTimeField(default=timezone.now)
    
class Comment(models.Model):
    # User who wrote the comment
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # The content of the comment
    content = models.TextField()
    # When the comment was posted
    posted_on = models.DateTimeField(default=timezone.now)
    # Ticket the comment is attached to
    associated_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
