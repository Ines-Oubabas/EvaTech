from django.contrib import admin
from .models import Student, Question, Submission, Teacher, Test

# Register Teacher model
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user')  # Display columns in the admin list view
    search_fields = ('name', 'email', 'user__username')  # Add search functionality

# Register Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user')
    search_fields = ('name', 'email', 'user__username')

# Register Question model
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test')  # Display the question text and the associated test
    search_fields = ('text', 'test__title')  # Enable searching by question text and test title

# Register Submission model
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'question', 'answer', 'is_correct')  # Show key details
    list_filter = ('is_correct',)  # Add filter by correctness
    search_fields = ('student__name', 'question__text')  # Add search functionality

# Register Test model
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'created_at')  # Display key fields
    search_fields = ('title', 'teacher__name')  # Add search functionality
    list_filter = ('created_at',)  # Add filter by creation date
