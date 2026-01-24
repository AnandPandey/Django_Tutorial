from django.contrib import admin
from .models import projectVariety,ProjectReview,Store,ProjectCertificate
# Register your models here.

class ProjectReviewInline(admin.TabularInline):
    model=ProjectReview
    extra=2
    
class projectVarietyAdmin(admin.ModelAdmin):
    list_display=('name', 'type', 'date_added')
    inlines = [ProjectReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display= ('name', 'location')
    filter_horizontal= ('project_varieties',)
    
class ProjectCertificateAdmin(admin.ModelAdmin):
    list_display= ('project', 'certificate_number')
    
admin.site.register(projectVariety, projectVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ProjectCertificate, ProjectCertificateAdmin)