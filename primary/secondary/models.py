from django.db import models

# Create your models here.

class Todos(models.Model):
    sno = models.AutoField(primary_key = True)
    desc = models.TextField()
    status = models.BooleanField(default = False)
    time_created = models.DateTimeField(auto_now = True)
    time_updated = models.DateTimeField(auto_now_add = True)
    
    def formated_time(self):
        return self.time_created.strftime("%I:%M%p").upper().replace(".","").replace("PM"," PM").replace("AM"," AM")