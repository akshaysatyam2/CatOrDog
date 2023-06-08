from django.shortcuts import render
import pickle

def home(request):
    return render(request, 'CheckCatOrDog/index.html')

def getPredictions(Country ,CreditScore,Gender, Age, Tenure,Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    cnn = pickle.load(open('ml_model.sav', 'rb'))



def result(request):

    img = (request.POST.get('img'))


    # print(f"Fetched {Country }")

    result = getPredictions(img)
    print(result)
    return render(request, 'CheckCatOrDog/result.html', {'result': result})