from django.db import models
from django.contrib.auth.models import User
# Problem Model Contains the Problem Info



from django.db import models

class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="Problem Name")
    description = models.TextField(verbose_name="Problem Description")
    difficulty = models.CharField(
        max_length=20, choices=DIFFICULTY_CHOICES, default='Easy', verbose_name="Difficulty Level"
    )
    tags = models.TextField(default="None", verbose_name="Tags (comma-separated)")
    code = models.TextField(default="No code provided", verbose_name="Starter Code")
    expectedTC = models.TextField(default="None", verbose_name="Expected Time Complexity")
    constraints = models.TextField(default="None", verbose_name="Constraints")

    def get_tags(self):
        """Convert the comma-separated string into a list of tags."""
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()] if self.tags else []

    def __str__(self):
        return self.name


class Testcase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="testcases")
    input = models.TextField(default="None", verbose_name="Input")
    output = models.TextField(default="None", verbose_name="Expected Output")

    def __str__(self):
        return f"{self.problem.name} - Test {self.pk}"

class CodeSubmission(models.Model):
    ProblemName = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    code = models.TextField()
    verdict = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)



