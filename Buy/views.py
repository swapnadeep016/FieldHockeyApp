from django.shortcuts import render,redirect
from django.http import HttpResponse
from Buy.models import User, Stadium, Ticket, RemainingTickets,Match
from . import forms

def buyTicket(uId, mId, sId, ty, count):
	ticketPrice = 0
	ticketType = 'Z'
	stadium = Stadium.objects.get(pk=sId)
	match = Match.objects.get(pk=mId)
	rTickets = RemainingTickets.objects.get(matchId=match)
	if ty == 'A':
		ticketType = 'A'
		ticketPrice = stadium.typeAPrice
		rTickets.typeARemaining = rTickets.typeARemaining - int(count)
	elif ty =='B':
		ticketType = 'B'
		ticketPrice = stadium.typeBPrice
		rTickets.typeBRemaining = rTickets.typeBRemaining - int(count)
	elif ty =='C':
		ticketType = 'C'
		ticketPrice = stadium.typeBPrice
		rTickets.typeCRemaining = rTickets.typeCRemaining - int(count)
	user = User.objects.get(pk=uId)
	t = Ticket(ticketType=ticketType, price=ticketPrice, userId=user, matchId=match)
	t.save()
	rTickets.save()


# Create your views here.

def index(request):
	all_matches = {'matches': Match.objects.all() }
	return render(request,'Buy/index.html',all_matches)
	# return HttpResponse("Hello World")

def match(request):
	mId = request.GET.get('matchid')
	m = Match.objects.get(pk=mId)
	st = m.stadiumId
	rem = RemainingTickets.objects.get(matchId=mId)
	dic = {"match" : m,
			"stadium" : st,
			"rem" : rem }
	return render(request,'Buy/match.html',dic)

def SignupFormView(request):
	form = forms.SignupForm()
	mId=request.GET.get('matchid')
	sId=request.GET.get('sid')
	ty = request.GET.get('type')
	count = request.GET.get('count')

	if request.method == 'POST':
		form = forms.SignupForm(request.POST)

		if form.is_valid():
			# DO SOMETHING CODE
			print("VALIDATION SUCCESS!")
			n = form.cleaned_data['name']
			em = form.cleaned_data['email']
			pas = form.cleaned_data['password']
			u = User(name=n, emailId=em, password=pas)
			u.save()
			buyTicket(u.pk, mId, sId, ty,count)
			return redirect('/final/')
		else:
			forms.SignupForm.raiseError()

	return render(request,'Buy/signup.html',{'form':form})

def LoginFormView(request):
	form = forms.LoginForm()
	mId=request.GET.get('matchid')
	sId=request.GET.get('sid')
	ty = request.GET.get('type')
	count = request.GET.get('count')
	
	if request.method == 'POST':
		form = forms.LoginForm(request.POST)
		form.is_valid()
		u = User.objects.get(emailId = form.cleaned_data['email'])
		if u.password == form.cleaned_data['password']:
			buyTicket(u.pk, mId, sId, ty,count)
			return redirect('/final/')
			#return render(request, 'Buy/final.html',{'name' : u.name})

		else:
			dic = {
				'form' : form,
				'matchid' : mId,
				'sid' : sId,
				'type' : ty,
				'count' : count,
				'error' : 'yes'
			}
			return render(request, 'Buy/login.html',dic)

	dic = {
			'form' : form,
			'matchid' : mId,
			'stadiumid' : sId,
			'ty' : ty,
			'error' : 'no'
	}
	return render(request, 'Buy/login.html',dic)

def finalPage(request):

	return render(request,'Buy/final.html',{})