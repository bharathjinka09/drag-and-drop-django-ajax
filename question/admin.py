from django.contrib import admin
from .models import Paper, Question, PaperQuestion
# Register your models here.

class PaperQuestionInline(admin.TabularInline):
    model = PaperQuestion
    extra = 1
    
@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    inlines = (PaperQuestionInline,)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

