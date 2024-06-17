from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string

tasks = {
    "monday":"Complete Python project",
    "tuesday":"Attend team meeting",
    "wednesday":"Go grocery shopping", 
    "thursday":"Work out at the gym", 
    "friday":"Read a book", 
    "saturday":"Clean the house", 
    "sunday":"Call family",
}

def index(request):
    # Render the 'challenges.html' template with the context
    tasklist = list(tasks.keys())
    return render(request, "challenges/challenges.html", {"tasklists": tasklist})

def challenges(request,month):

    try:
        return render(request, "challenges/task.html", {"day": month,"task":tasks[month]})
    
    except:
        raise Http404()

def numberchallenge(request,num):

    try:
        tasks_list = list(tasks.keys())
        redirect_month = tasks_list[num -1]
        redirect_path = reverse("month-path",args=[redirect_month])

        return HttpResponseRedirect(redirect_path)

    except:
        raise Http404()
