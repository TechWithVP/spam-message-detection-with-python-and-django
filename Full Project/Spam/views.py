from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
import os
import joblib

model1 = joblib.load(os.path.dirname(__file__) + "\\mySVCModel1.pkl")
model2 = joblib.load(os.path.dirname(__file__) + "\\myModel.pkl")

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if(request.method == "POST"):
        un = request.POST.get('username')
        up = request.POST.get('password')
        
        if(un == "techwithvp" and up == "techwithvp"):
            request.session['authdetails'] = "techwithvp"
            if(request.session['authdetails'] == "techwithvp"):
                return render(request, 'index.html')
            else:
                return redirect('/auth')
        else:
            return render(request, 'auth.html')
    else:
        if(request.session.has_key('authdetails') == True):
            print("Session Auth")
            return render(request, 'index.html')
        else:
            return render(request, 'auth.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def checkSpam(request):
    if(request.method == "POST"):
        if(request.session['authdetails'] == "techwithvp"):
            algo = request.POST.get("algo")
            rawData = request.POST.get("rawdata")

            if(algo == "Algo-1"):
                return render(request, 'output.html', {"answer" : model1.predict([rawData])[0]})
            elif(algo == "Algo-2"):
                return render(request, 'output.html', {"answer" : model2.predict([rawData])[0]})
        else:
            return redirect('/')
    else:
        return render(request, 'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    if(request.session.has_key('authdetails') == True):
        request.session.clear()
        print("-----------------")
        # request.session.flush()
        return redirect('/')
    else:
        return redirect('/')