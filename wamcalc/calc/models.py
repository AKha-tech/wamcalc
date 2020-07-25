from django.db import models

# Create your models here.
class Marks(models.Model):
    name = models.CharField(max_length=120, null=True, default="")
    code = models.CharField(max_length=8)
    mark = models.DecimalField(decimal_places=2, max_digits=4)
    cp = models.IntegerField()

    def passed(self):
        if self.mark >= 50:
            return True
        return False

    def letter(self):
        if 80 <= self.mark <= 100:
            return 'HD'
        
        elif 70 <= self.mark < 80:
            return 'D'

        elif 60 <= self.mark < 70:
            return 'C'

        elif 50 <= self.mark < 60:
            return 'P'
        
        else:
            return 'F'