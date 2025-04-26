from django.contrib import admin
from problems.models import Problem
from problems.models import Testcase
from problems.models import CodeSubmission


admin.site.register(Problem)
admin.site.register(Testcase)

class CodeSubmissionAdmin(admin.ModelAdmin):
    # Include the 'timestamp' field in the list display
    list_display = ('ProblemName', 'user', 'language', 'timestamp', 'verdict')
admin.site.register(CodeSubmission, CodeSubmissionAdmin)


# Register your models here.
