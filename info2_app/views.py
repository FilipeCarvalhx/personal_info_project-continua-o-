from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

# Create your views here.

def welcome(request):
        return JsonResponse({"message": "Welcome to the Personal Info API!"})


def goodbye(request):
        return JsonResponse({"message": "Goodbye, see you next time!!"})


def current_time(request):
        now = datetime.now().strftime("%H:%M:%S")
        return JsonResponse({"current_time": now})

 ##Nome   
def greet_Name(request):
        name = request.GET.get("name")
        if name:
            return JsonResponse({"message": f"Hello, {name}!"})
        else:
            return JsonResponse({"message": "Hello, Stranger!"})
        

##Idade
def age_category(request):
        
    age = request.GET.get("age")

    if age is None:
        return JsonResponse({"error": "Missing 'age' parameter."}, status=400)

    try:
        age = int(age)
    except ValueError:
        return JsonResponse({"error": "Invalid 'age' value. Must be an integer."}, status=400)

    if age <= 12:
        category = "Child"
    elif age <= 17:
        category = "Teenager"
    elif age <= 59:
        category = "Adult"
    else:
        category = "Senior"

    return JsonResponse({"category": category})
## Soma
def sum_numbers(request, num1, num2):
    try:
        n1 = int(num1)
        n2 = int(num2)
    except ValueError:
        return JsonResponse(
            {"error": "Invalid input, please provide two integers."}, status=400
        )

    return JsonResponse({"sum": n1 + n2})


    
