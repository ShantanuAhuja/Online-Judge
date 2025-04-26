"""
URL configuration for onlinejudge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the dinclude() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from userActivity.views import showUserSubmission
from userActivity.views import showParticularSubmission
from userActivity.views import showLeaderboard

urlpatterns = [
    path('submission/', showUserSubmission),
    path('submission/<int:id>/', showParticularSubmission),
    path('leaderboard/',showLeaderboard),
]
