from django.contrib import admin

# Register your models here.
from analytics.models import Base,Department,Channel,Employee, Organization,Post
admin.site.register(Base)
admin.site.register(Department)
admin.site.register(Channel)
admin.site.register(Employee)
admin.site.register(Post)
admin.site.register(Organization)