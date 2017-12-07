import os
import random
import sqlite3

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate


@csrf_exempt
def home(request):
    image = sqlite3.connect("test.db")
    cursor = image.cursor()
    if request.method == 'POST':
        if request.POST.get('win','') == request.POST.get('id1',''):
            winer = int(request.POST.get('id1',''))
            loser = int(request.POST.get('id2', ''))
        else:
            winer = int(request.POST.get('id2', ''))
            loser = int(request.POST.get('id1', ''))
        cursor.execute("SELECT rate FROM photo WHERE id = (?)", (winer,))
        Ra = cursor.fetchone()
        Ra = Ra[0]
        cursor.execute("SELECT rate FROM photo WHERE id = (?)", (loser,))
        Rb = cursor.fetchone()
        Rb = Rb[0]
        winner_rate = Ra + 40 * (1 - 1 / (1 + 10 ** ((Rb - Ra) / 400)))
        losser_rate = Rb + 40 * (0 - 1 / (1 + 10 ** ((Ra - Rb) / 400)))
        cursor.execute("UPDATE photo SET rate = ? WHERE id = ?", (int(winner_rate), winer,))
        cursor.execute("UPDATE photo SET rate = ? WHERE id = ?", (int(losser_rate), loser,))
        image.commit()

    cursor.execute("SELECT photo, id FROM photo ORDER BY RANDOM() LIMIT  2")
    row = cursor.fetchall()
    args = {}
    args["id1"] = row[0][1]
    args["id2"] = row[1][1]
    args["image1"] = row[0][0]
    args["image2"] = row[1][0]
    args['username'] = auth.get_user(request).username
    image.close()
    return render_to_response('home.html', args)

def about(request):
    return render(request, 'about.html')

def top(request):
    image = sqlite3.connect("test.db")
    cursor = image.cursor()
    cursor.execute("SELECT photo FROM photo ORDER BY rate")
    row = cursor.fetchall()
    args = {}
    args["image1"] = row[0][0]
    args["image2"] = row[1][0]
    args["image3"] = row[2][0]
    args["image4"] = row[3][0]
    args["image5"] = row[4][0]
    args["image6"] = row[5][0]
    args["image7"] = row[6][0]
    args["image8"] = row[7][0]
    args["image9"] = row[8][0]
    args["image10"] = row[9][0]
    args['username'] = auth.get_user(request).username
    image.close()
    return render_to_response('top.html', args)

@csrf_exempt
def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            args['login_error'] = "User not found"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')