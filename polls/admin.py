from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    exita = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {'fields': ['question_text']}
        ),
        (
            'Date information',
            {
                'fields': ['pub_date'],
                'classes': ['collapse']
            }
        ),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    seach_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
