from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from problems.models import CodeSubmission
from problems.models import Problem
from django.contrib.auth.models import User
from django.http import HttpResponse
import os
from typing import Dict


# Create your views here.
@ login_required
def showUserSubmission(request):

    user= request.user
    submissions = CodeSubmission.objects.filter(user=user).order_by('-timestamp')[:10]

    return render(request, 'userSubmissions.html', {'submissions': submissions})


@login_required
def showParticularSubmission(request, id):
    print(id)
    submission = CodeSubmission.objects.get(id=id)
    userCodePath = submission.code
    if os.path.exists(userCodePath):
        try:
            # Open and read the file content
            with open(userCodePath, 'r') as file:
                file_content = file.read()

                context = {
                    'submission': submission,
                    'file_content': file_content,  # Pass the file content to the template
                }

            # Pass the file content to the template
            return render(request, 'particularCodeSubmission.html', context)

        except Exception as e:
            # Handle the error if there is an issue reading the file
            return HttpResponse(f"Error reading file: {e}", status=500)
    else:
        return HttpResponse("File not found", status=404)


def showLeaderboard(request):
    users = User.objects.all()
    user_map: Dict[str, int] = {}
    for user in users:
        submissions = CodeSubmission.objects.filter(user=user)
        my_map: Dict[str, int] = {}
        score = 0
        for submission in submissions:
            if submission.verdict == "Accepted":
                problem = Problem.objects.get(name=submission.ProblemName)
                my_map[problem.name]=1;

        user_map[user.username] = len(my_map) *100
    sorted_user_map = dict(sorted(user_map.items(), key=lambda item: item[1], reverse=True))
    return render(request, 'leaderboard.html', {'user_map': sorted_user_map})


