from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import Employee
from .forms import EmployeeForm
from .models import Post
from .models import Awards



def home(request):
    return render(request, 'tables/home.html')


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            post_id = request.POST.get('post')
            award_id = request.POST.get('award')

            employees = Employee.objects.filter(name__icontains=name)

            if post_id:
                employees = employees.filter(fk_post_id=post_id)

            if award_id:
                employees = employees.filter(fk_awards_id=award_id)

            return render(request, 'tables/employee_search_results.html', {'employees': employees})
    else:
        form = SearchForm()

    posts = Post.objects.all()  # Add this line to fetch all posts
    awards = Awards.objects.all()  # Add this line to fetch all awards

    return render(request, 'tables/search.html', {'form': form, 'posts': posts, 'awards': awards})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Перенаправление на домашнюю страницу или другую нужную страницу
    else:
        form = EmployeeForm()
    return render(request, 'tables/add.html', {'form': form})
