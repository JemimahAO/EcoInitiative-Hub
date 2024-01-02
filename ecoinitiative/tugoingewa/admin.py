from django.contrib import admin
from .models import Event, Story, Initiative, Comments, Contact

class EventAdmin(admin.ModelAdmin):
    pass

class StoryAdmin(admin.ModelAdmin):
    pass

class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'date_created')
    list_filter = ('status',)
    search_fields = ['title', 'description', 'goals']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Event, EventAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Comments)
admin.site.register(Contact)