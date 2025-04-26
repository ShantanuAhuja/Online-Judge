from django.shortcuts import render
from problems .models import Problem
from django.contrib.auth.decorators import login_required# Create your views here.


def renderProblemsApi(request):
    problems = Problem.objects.all()
    return render(request, 'problemsPage.html',{'problems':problems})

def renderProblemsDetailsApi(request,name):
    req_problem=Problem.objects.get(name=name)
    description = req_problem.description
    print(description)
    testcases = req_problem.testcases.all()[:2]
    tags_list = req_problem.get_tags()

    boiler_plate = {
"C":"""
#include <stdio.h>


int main() {
    printf("Hello Coder!");
    return 0;
}""",
    
    "CPP": """
#include<iostream>
using namespace std;


int main() {
    cout << "Hello Coder!";
    return 0;
}""",
    
    "Java": """
class Main {
  public static void main(String[] args) {
    System.out.println("Hello Coder!");
  }
}""",
    
    "Py": """
print("Hello Geek!")"""
}

    
    return render(request, 'problemsDetails.html',{'problem':req_problem,"tags_list": tags_list,"testcases":testcases,"boiler_plate":boiler_plate})





