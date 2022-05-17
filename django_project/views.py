from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth import logout
from accounts.models import UserModel

import os.path

#from data import checkRes
from django_project.data import checkRes


from django.template import RequestContext


from django.template.loader import get_template
from django.db import models

#python manage.py makemigrations

#python manage.py migrate --run-syncdb


num_page = 1


def add_task_to_list(request, name, id):
    dl = False
    if(dl):
        UserModel.objects.all().filter(iduser=1).delete()
        UserModel.objects.all().filter(iduser=2).delete()
        UserModel.objects.all().filter(iduser=3).delete()

    global num_page

    current_user = request.user.username
    if(request.method == "POST" and 'run_script' in request.POST):
        us = UserModel.objects.all().filter(iduser=id)
        res = checkRes(request, us[0], num_page)
        print(us[0].lessonsmax, num_page)
        print(res,  num_page, 'post', 'add_task_to_list')
        if(res):
            return render(request, 'lessons'+str(num_page)+'.html',
                          {'num': num_page, 'name': us[0].name, 'id': us[0].iduser, 'isres': 1})
        else:
            return render(request, 'lessons' + str(num_page) + '.html',
                          {'num': num_page, 'name': us[0].name, 'id': us[0].iduser, 'isres': 2})


    if(current_user == name):
        cn = UserModel.objects.all().filter(iduser=id).count()
        if(cn == 0):
            u = UserModel(iduser=id, name=name)
            u.save()
        us = UserModel.objects.all().filter(iduser=id)
        num_page = us[0].lessonsmax
        return render(request, 'lessons'+str(us[0].lessonsmax)+'.html', {'num': us[0].lessonsmax, 'name': us[0].name, 'id': us[0].iduser, 'isres': 0})
    else:
        logout(request)
        return render(request, 'home.html')

def next_lesson(request, idlesson, iduser, namep, isres):

    current_user = request.user.username
    global num_page

    if (request.method == "POST" and 'run_script' in request.POST):
        us = UserModel.objects.all().filter(iduser=iduser)
        res = False
        res = checkRes(request, us[0], num_page, num_page == us[0].lessonsmax)
        print(us[0].lessonsmax, num_page)
        print(num_page, 'POST', 'next_lesson')

        if (res):
            return render(request, 'lessons' + str(num_page) + '.html',
                          {'num': num_page, 'name': us[0].name, 'id': us[0].iduser, 'isres': 1})
        else:
            return render(request, 'lessons' + str(num_page) + '.html',
                          {'num': num_page, 'name': us[0].name, 'id': us[0].iduser, 'isres': 2})

    numpage = idlesson

    numpage = idlesson + 1
    isexist = os.path.exists('templates/lessons' + str(numpage) + '.html')

    if(isexist):
        us = UserModel.objects.all().filter(iduser=iduser)

        isres = 0
        if (us[0].lessonsmax > numpage):
            isres = 1
        print(us[0].lessonsmax, numpage, '<<<<<<<<<<<<<<<<<<<<<<')
        num_page = numpage
        print(num_page, 'get', 'next_lesson')
        return render(request, 'lessons' + str(numpage) + '.html',
                  {'num': numpage, 'name': namep, 'id': iduser, 'isres': isres})
    else:
        return error_404(request, {}) #render(request, '404.html')

def old_lessons(request, idlesson, iduser, namep):
    global num_page
    print('old lessons', idlesson, num_page)


    if (request.method == "POST" and 'run_script' in request.POST):
        us = UserModel.objects.all().filter(iduser=iduser)
        ud= us[0]
        ud.lessonsmax = num_page
        res = checkRes(request, ud, num_page, False)
        print(us[0].lessonsmax, num_page)
        print('old_lessons', 'post', res)
        np = idlesson
        if (np != 1):
            np = idlesson - 1
        num_page = np
        if(res):
            isres = 1
        else:
            isres = 4

        if (res):
            return render(request, 'lessons' + str(np) + '.html',
                          {'num': np, 'name': us[0].name, 'id': us[0].iduser, 'isres': isres})
        else:
            return render(request, 'lessons' + str(np) + '.html',
                          {'num': np, 'name': us[0].name, 'id': us[0].iduser, 'isres': isres})


    np = idlesson - 1
    num_page = np
    print(num_page, 'old_lessons', 'get')
    if(np > 0):
        return render(request, 'lessons' + str(np) + '.html', {'num': np, 'name': namep, 'id': iduser, 'isres': 1})
    else:
        return render(request, 'lessons' + str(idlesson) + '.html',
                          {'num': idlesson, 'name': namep, 'id': iduser, 'isres': 4})



def error_404(request, context):
    context = {}
    return render(request, '404.html', context)



