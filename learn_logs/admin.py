from django.contrib import admin

# Register your models here.
from learn_logs.models import Topic
admin.site.register(Topic)
from learn_logs.models import Entry
admin.site.register(Entry)

