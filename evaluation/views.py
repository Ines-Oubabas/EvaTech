from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .models import Question, Submission, Student, Teacher, Test
from .forms import SignupForm, TestForm

# Page d'accueil
def home(request):
    return render(request, 'home.html')

# Page d'inscription
def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data['is_teacher']:
                Teacher.objects.create(user=user, name=user.username, email=user.email)
            else:
                Student.objects.create(user=user, name=user.username, email=user.email)
            login(request, user)
            messages.success(request, "Inscription réussie ! Bienvenue sur votre tableau de bord.")
            return redirect('dashboard')
        else:
            messages.error(request, "Une erreur est survenue. Veuillez vérifier les informations saisies.")
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})

# Tableau de bord étudiant
@login_required
def dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, "Aucun étudiant trouvé pour cet utilisateur.")
        return redirect('home')

    if not request.session.get('welcome_shown', False):
        messages.success(request, "Bienvenue dans votre tableau de bord !")
        request.session['welcome_shown'] = True

    submissions = Submission.objects.filter(student=student)
    return render(request, 'dashboard.html', {'submissions': submissions})

# Tableau de bord enseignant
@login_required
def teacher_dashboard(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "Aucun enseignant trouvé pour cet utilisateur.")
        return redirect('home')

    tests = Test.objects.filter(teacher=teacher)
    return render(request, 'teacher_dashboard.html', {'tests': tests})

# Création de test
@login_required
def create_test(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        messages.error(request, "Aucun enseignant trouvé pour cet utilisateur.")
        return redirect('home')

    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.teacher = teacher
            test.save()
            messages.success(request, "Test créé avec succès.")
            return redirect('teacher_dashboard')
    else:
        form = TestForm()

    return render(request, 'create_test.html', {'form': form})

# Liste des tests disponibles
@login_required
def available_tests(request):
    tests = Test.objects.all()
    return render(request, 'available_tests.html', {'tests': tests})

# Page de questions
@login_required
def question_page(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, "Aucun étudiant trouvé pour cet utilisateur.")
        return redirect('home')

    if request.method == 'POST':
        for question in Question.objects.all():
            answer = request.POST.get(f'answer_{question.id}')
            is_correct = (answer == question.correct_answer)
            
            submission, created = Submission.objects.get_or_create(
                student=student,
                question=question,
                defaults={'answer': answer, 'is_correct': is_correct}
            )
            if not created:
                submission.answer = answer
                submission.is_correct = is_correct
                submission.save()

        messages.success(request, "Merci pour vos réponses ! Consultez vos résultats.")
        return redirect('result_page')

    questions = Question.objects.all()
    return render(request, 'question_page.html', {'questions': questions})

# Page de résultats
@login_required
def result_page(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, "Aucun étudiant trouvé pour cet utilisateur.")
        return redirect('home')

    submissions = Submission.objects.filter(student=student)
    return render(request, 'result_page.html', {'submissions': submissions})
