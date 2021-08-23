from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
import django.contrib.auth.forms
import pandas as pd
import os

def chatbot(request):
    return render(request, 'chatbot.html', {'name' : 'Taurius'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'user.html', {"Result" : res})

class HomePageView(TemplateView):
    template_name = 'home.html'

def process(request):
    msg = request.POST['msg'].lower()
    print(msg)
    x=msg.split()
    want=''
    disease=''
    index = 0
    filename = os.path.join((os.path.dirname(os.path.abspath(__file__))), 'data.csv')
    data = pd.read_csv(filename)
    for i in x:
        if(i=='symptoms' or i=='precautions' or i=='medications'):
            want=i
        if(disease==''):
            index=0
            for j in data.get('Disease'):
                if j == i:
                    disease=j
                    break
                else:
                    index += 1
    # if(len(msg.split())>1):
    #     want = msg.rsplit(' ', 1)[1]
    # disease = msg.rsplit(' ', 1)[0]

    # print(disease)
    # print(want)
    # print(index)
    print(data.get('precautions')[index])
    if(want==''):
        html='<h1>Symptoms: </h1><h2>'+data.get('symptoms')[index]+'</h2> <h1>Precautions: </h1><h2>'+data.get('precautions')[index]+'</h2><h1>Medications: </h1><h2>'+data.get('medications')[index]+'</h2>'
        # return HttpResponse('Symptoms: '+data.get('symptoms')[index]+"\n\n"+'Precautions: '+data.get('precautions')[index]+'\n\nMedications: '+data.get('medications')[index])
        return HttpResponse(html)
    if(want!=''):
        return HttpResponse(data.get(want)[index])

    # if "Location".lower() in msg:
    #     latlong = "show"
    #     #tts(text="Please refer to the map")
    #     return HttpResponse(latlong)
    text = "Sorry can't understand what you are saying."
    return HttpResponse(text)


def signup(request):
    if request.method == 'POST':
        form = django.contrib.auth.forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'chatbot.html')
    else:
        form = django.contrib.auth.forms.UserCreationForm()
    return render(request, 'signup.html', {'form': form})