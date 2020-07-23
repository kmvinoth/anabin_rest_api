from django.db import models

# Create your models here.
class Institutions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    institution = models.CharField(max_length=1024, blank=True, null=True)
    city_or_place = models.CharField(max_length=1024, blank=True, null=True)
    institution_type = models.CharField(max_length=1024, blank=True, null=True)
    status = models.CharField(max_length=1024, blank=True, null=True)
    country = models.CharField(max_length=1024, blank=True, null=True)
    further_details = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.id, self.institution, self.ort, self.institutions_typ, 
        self.status, self.land, self.gehort_zur_institution)
    
    def get_institution(self):
        return self.id + 'belongs to ' + self.institution

    class Meta:
        managed = False
        db_table = 'anabin_all_countries'
        verbose_name_plural = 'Institutions'
        ordering = ['pk']
        app_label  = 'anabin'