from django.db import models

class Job(models.Model):
    WEEKDAYS = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    schedule_days = models.JSONField()  # Store a list of weekdays
    schedule_time = models.TimeField()  # Time the job is executed on the selected days

    def __str__(self):
        return self.name


class Script(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='scripts')
    name = models.CharField(max_length=255)
    content = models.TextField()  # This will store the code
    table_name = models.CharField(max_length=255)
    order_exec = models.PositiveIntegerField()
    import_enabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['order_exec']
