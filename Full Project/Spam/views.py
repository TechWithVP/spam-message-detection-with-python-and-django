from django.shortcuts import render
from django.http import HttpResponse
import os
import joblib

model1 = joblib.load(os.path.dirname(__file__) + "\\mySVCModel1.pkl")
model2 = joblib.load(os.path.dirname(__file__) + "\\myModel.pkl")

# Create your views here.
def index(request):
    return render(request, 'index.html')

def checkSpam(request):
    if(request.method == "POST"):
        
        algo = request.POST.get("algo")
        rawData = request.POST.get("rawdata")

        if(algo == "Algo-1"):
            return render(request, 'output.html', {"answer" : model1.predict([rawData])[0]})
        elif(algo == "Algo-2"):
            return render(request, 'output.html', {"answer" : model2.predict([rawData])[0]})
    else:
        return render(request, 'index.html')