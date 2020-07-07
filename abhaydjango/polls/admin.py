from django.contrib import admin

# Register your models here.
from .models import Question,Choice


admin.site.site_header = 'Polls Page Admin'

admin.site.site_title = 'Polls Admin  Area'


admin.site.index_title = 'Welcome to Polls Admin Area'
#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'],'classes':['collaps']}),]
    inlines=[ChoiceInline]


admin.site.register(Question,QuestionAdmin)