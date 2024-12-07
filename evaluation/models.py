from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    # Relation avec l'utilisateur de Django pour utiliser le système d'authentification intégré
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    # Relation avec l'utilisateur pour les enseignants
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    # Un enseignant peut créer plusieurs tests
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="tests")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    # Les questions sont associées à un test
    text = models.TextField()
    correct_answer = models.CharField(max_length=100)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions", null=True)

    def __str__(self):
        return self.text

class Submission(models.Model):
    # Les réponses des étudiants
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="submissions")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="submissions")
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.question.text[:50]}"

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"

class StudentAnswer(models.Model):
    # Les réponses des étudiants pour chaque test
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="answers")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.submission.student.name} - {self.question.text[:50]}"
