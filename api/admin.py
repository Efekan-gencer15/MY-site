from django.contrib import admin
from api.models import Project, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'created_at')
    list_filter = ('technologies', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    ordering = ('-created_at',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'linkedin', 'github') 