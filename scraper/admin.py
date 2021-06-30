from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(RandomDomainGenerator)
admin.site.register(ScrapedDeletedDomain)
admin.site.register(GodaddyAppraisal)