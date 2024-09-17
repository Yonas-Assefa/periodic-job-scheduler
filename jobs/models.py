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
    schedule_days = models.JSONField()  
    schedule_time = models.TimeField()  

    def __str__(self):
        return self.name
    


class Script(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='scripts')
    script_name = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)  # This will store the code
    table_name = models.CharField(max_length=255)
    order_exec = models.PositiveIntegerField()
    import_enabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['order_exec']
    def __str__(self):
        return self.script_name
    

    @classmethod
    def reorder_scripts(cls, job_id):
        scripts = cls.objects.filter(job_id=job_id).order_by('order_exec', 'id')
        expected_order = 1
        changes_made = False
        for script in scripts:
            if script.order_exec != expected_order:
                script.order_exec = expected_order
                script.save(update_fields=['order_exec'])
                changes_made = True
        expected_order += 1
        return changes_made
    

