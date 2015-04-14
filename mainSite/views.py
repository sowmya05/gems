from django.shortcuts import render_to_response, render
from mainSite.models import *
import json
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .databaseManager import getCandidateDetail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def user_login(request):                      #url for login page is home/login
    if request.method == 'POST':
    	username= request.POST.get('username')
    	password = request.POST.get('password')
    	user = authenticate(username=username,password=password)
    	if user:
    	    if (user.is_active and user.is_staff):
    	        login(request, user)
    	        return HttpResponseRedirect('/gems/admin')
    	    else:
                login(request, user)
                return HttpResponseRedirect('/gems/voterHome')
    	else:
    	    return HttpResponse("your account is diabled")		
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})		
    return render(request, 'index.html', context_dict)

@login_required
def voterHome(request):
	return render(request, 'main_page.html')

def view_candidate(request):
    	candidate_i = New_Candidate.objects.all()
	candidate_data = {
		"candidate_detail" : candidate_i
	}
	return render_to_response('view_candidates.html', candidate_data, context_instance=RequestContext(request))

def candidateView(request,candidateName):
	b = New_Candidate.objects.get(name=candidateName)
	data = {
		"detail" : b
	}
	#candidateDetails = getCandidateDetail(candidateName)
	#contextObj = Context({'candidateName':candidateName,'candidateDetails':candidateDetails})
	return render_to_response('test.html',data,context_instance=RequestContext(request))

def register(request):
	return render(request, 'registration_form.html')

def add_candidate(request):
	if request.GET:
		new_candidate = New_Candidate(name=request.GET['name'],post=request.GET['optionsRadios'],  roll=request.GET['roll'], department=request.GET['dept'], cpi=request.GET['cpi'], sem=request.GET['sem'], backlogs=request.GET['back'], email=request.GET['email'], contact=request.GET['contact'], hostel=request.GET['hostel'], room=request.GET['room'], agenda=request.GET['agenda'])
        	new_candidate.save()
	return HttpResponseRedirect('/main')

def adminView(request):
    contexObj = Context({'dashAct':True,'nomniaAct':False,'discussAct':False,'startAct':False,'ipAct':False,'monitorAct':False,'resultAct':False,'pagetitle':'Home'})
    return render_to_response('Admin/adminDash.html',contexObj)

def discuss(request):
    contexObj = Context({'dashAct':False,'nomniaAct':False,'discussAct':True,'startAct':False,'ipAct':False,'monitorAct':False,'resultAct':False,'pagetitle':'Discussion'})
    return render_to_response('Admin/Discussion.html',contexObj)

def adminResultsView(request):

    contexObj = Context({'dashAct':False,'nomniaAct':False,'discussAct':False,'startAct':False,'ipAct':False,'monitorAct':False,'resultAct':True,'pagetitle':'Results'})
    return render_to_response('Admin/Results.html',contexObj)



def adminStartStop(request):
    contexObj = Context({'dashAct':False,'nomniaAct':False,'discussAct':False,'startAct':True,'ipAct':False,'monitorAct':False,'resultAct':False,'pagetitle':'Start/Stop'})
    return render_to_response('Admin/StartStop.html',contexObj)


def adminIPView(request):
    contexObj = Context({'dashAct':False,'nomniaAct':False,'discussAct':False,'startAct':False,'ipAct':True,'monitorAct':False,'resultAct':False,'pagetitle':'View Allowed IPs'})
    return render_to_response('Admin/adminIPs.html',contexObj)

def adminMonitorView(request):
    contexObj = Context({'dashAct':False,'nomniaAct':False,'discussAct':False,'startAct':False,'ipAct':False,'monitorAct':True,'resultAct':False,'pagetitle':'Monitor Elections'})
    return render_to_response('Admin/adminMonitor.html',contexObj)

def adminNominaView(request):
    contexObj = Context({'dashAct':False,'nomniaAct':True,'discussAct':False,'startAct':False,'ipAct':False,'monitorAct':False,'resultAct':False,'pagetitle':'Nominations'})
    return render_to_response('Admin/adminNomina.html',contexObj)