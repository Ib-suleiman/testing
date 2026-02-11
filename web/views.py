from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, School
from .forms import BookForm, SchoolForm, CreateUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    school_query = request.GET.get('school_search')
    book_query = request.GET.get('book_search')

    schools_list = School.objects.all()
    books_list = Book.objects.all()

    if school_query:
        schools_list = schools_list.filter(
            Q(name__icontains=school_query) |
            Q(location__icontains=school_query)
        )

    if book_query:
        books_list = books_list.filter(
            Q(title__icontains=book_query) |
            Q(author__icontains=book_query)
        )

    school_paginator = Paginator(schools_list, 5)  # 5 per page
    book_paginator = Paginator(books_list, 5)

    school_page_number = request.GET.get('school_page')
    book_page_number = request.GET.get('book_page')

    schools = school_paginator.get_page(school_page_number)
    books = book_paginator.get_page(book_page_number)

    context = {
        'schools': schools,
        'books': books,
        'total_schools': schools_list.count(),
        'total_books': books_list.count(),
    }

    return render(request, 'web/home.html', context)


def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin, login_url='home')
def add_Book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("An error occured")
    context = {'form': form}
    return render(request, 'web/addbook.html', context)


@user_passes_test(is_admin, login_url='home')
def add_school(request):
    form = SchoolForm()
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("An error occured")
    context = {'form': form}
    return render(request, 'web/addschool.html', context)


@user_passes_test(is_admin, login_url='home')
def edit_book(request, id):
    book = Book.objects.get(id = id)
    form = BookForm(instance = book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("Ann error Occured")
    context = {'form': form}
    return render(request, 'web/editbook.html', context)



@user_passes_test(is_admin, login_url='home')
def edit_school(request, id):
    school = School.objects.get(id = id)
    form = SchoolForm(instance = school)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance = school)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("An error occured")
    context = {'form': form}
    return render(request, 'web/editschool.html', context)


@user_passes_test(is_admin, login_url='home')
def delete_book(request, id):
    book = Book.objects.get(id = id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    context = {'book': book}
    return render(request, 'web/deletebook.html', context)


@user_passes_test(is_admin, login_url='home')
def delete_school(request, id):
    school = School.objects.get(id = id)
    if request.method == 'POST':
        school.delete()
        return redirect('home')
    context = {'school': school}
    return render(request, 'web/deleteschool.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login details")
    
    return render(request, 'web/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')



from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

def register(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account'

            message = render_to_string('web/email_verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            email = EmailMessage(
                mail_subject,
                message,
                to=[user.email]
            )
            email.send()

            return render(request, 'web/email_sent.html')
    else:
        form = CreateUser()

    return render(request, 'web/register.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'web/activation_success.html')
    else:
        return render(request, 'web/activation_invalid.html')