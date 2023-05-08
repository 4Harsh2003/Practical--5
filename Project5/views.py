from django.shortcuts import render
def Base(request):
    return render(request, 'Base.html',{})
def Child1(request):
    return render(request, 'Child1.html',{})
def Child2(request):
    return render(request, 'Child2.html',{})
