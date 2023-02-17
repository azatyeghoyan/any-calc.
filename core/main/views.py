from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def calculator(request):
    return render(request, 'calculator.html')

def factorial(request):
    return render(request, 'factorial.html')

def fibonacci(request):
    return render(request, 'fibonacci.html')

def calc_res(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    char = request.POST['char']
    if char == '+':
        res = num1 + num2
    elif char == '-':
        res = num1 - num2
    elif char == '*':
        res = num1 * num2
    elif char == '/':
        res = num1 / num2
    return render(request, 'result.html', {'res':res})

def fact_res(request):
    n = int(request.POST['n'])
    res = 1 
    for i in range(1, n + 1):
        res *= i
        return render(request, 'result.html', {'res':res})

def fib_res(request):
    n = int(request.POST['n'])
    n1 = 0
    n2 = 1
    for i in range(2, n + 1):
        res = n1 + n2
        n1 = n2
        n2 = res
    return render(request, 'result.html', {'res':res})
