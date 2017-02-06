from django.http import HttpResponse
#from .models import *
from .forms import *
from django.forms import modelformset_factory
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test


def login_view(request):
    if request.POST:
        if 'crypt_password' in request.POST:
            form = LoginForm(request)
            username = request.POST['id_no']
            password = request.POST['crypt_password']
            user = authenticate(username=username, password=password)
            if not user is None:
                login(request, user)
                return HttpResponseRedirect('/feedback/admin')
            else:
                return HttpResponse("Invalid Authentication")
        else:
            form2 = RegistrationForm(request)
            username = request.POST['id_no']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 != password2:
                return HttpResponse("Passwords Mismatch")
            if len(username) != 10:
                return HttpResponse("Invalid Username")
            User.objects.create_user(username.upper(),'example@gmail.com',password1).save()
            return HttpResponse("<h1>Successfully Registered</h1>")
    else:
        form = LoginForm()
        form2 = RegistrationForm()
    return render_to_response("login.htm", {'form': form,'form2':  form2 })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('login')


@login_required
def index(request):
    return HttpResponse("hello " + request.user.username)


@login_required
def admin(request):
    return render_to_response("admin.htm", {'username': request.user.username})


@login_required 
def academic_year(request):

    entries = 1
    myformset = modelformset_factory(AcademicYear, AcademicYearForm, extra=entries)
    formset=myformset(queryset=AcademicYear.objects.none())
    countform = FieldCountForm()
    deleteform = DeleteForm()
    if 'academic_year_code' in request.POST:
        try:
            AcademicYear.objects.get(academic_year_code=int(request.POST['academic_year_code'])).delete()
        except:
            error = "Year code does not exist"
            return render_to_response('academic_year.htm',
                                      {'formset': formset, 'countform': countform, 'deleteform': deleteform,
                                       'error': error, 'database': myformset(), 'username': request.user.username})
    if 'count' in request.POST:
        entries = int(request.POST['count'])
        myformset = modelformset_factory(AcademicYear, AcademicYearForm, extra=entries)
    if 'form-INITIAL_FORMS' in request.POST:
        formset = myformset(request.POST, queryset=AcademicYear.objects.none())
        if formset.is_valid():
            formset.save()
            #print(formset)
            formset = myformset(queryset=AcademicYear.objects.none())
        else:
            error = "Already exists"
            return render_to_response('academic_year.htm',
                                      {'formset': formset, 'countform': countform, 'deleteform': deleteform,
                                       'error': error, 'database': myformset(), 'username': request.user.username})
    else:
        formset = myformset(queryset=AcademicYear.objects.none())
        countform = FieldCountForm()
        deleteform = DeleteForm()

    return render_to_response('academic_year.htm', {'formset': formset, 'countform': countform,
                                                    'deleteform': deleteform, 'database': myformset(),
                                                    'username': request.user.username})


def display(request):
    form = modelformset_factory(AcademicYear, AcademicYearForm)()
    return render_to_response('display.html', {'display': form})
