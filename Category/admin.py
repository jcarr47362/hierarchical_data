from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from Category.models import Category

admin.site.register(Category, DraggableMPTTAdmin)



