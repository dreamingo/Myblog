from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from myblog.models import * 
from myblog.forms import * 
import md5
from basic import *

def test(request, id):
	var = varInit(0)
	if str(id) == '1':
		return redirect('index.html')
	else:
		return redirect('article.html')

def login(request):
	var = varInit(0)
	if request.session.get('has_login'):
		return redirect("/index/", permanent=True)

	else:
		if request.method == 'POST':
			var['loginForm'] = LoginForm(request.POST)
			if var['loginForm'].is_valid():
				try:
					p = User.objects.get(name=request.POST['name'])
					if(p.password == md5.md5(str(request.POST['password'])+"love").hexdigest()):
						request.session['has_login'] = True
						request.session['name'] = request.POST['name']
						return redirect("/index/", permanent=True)
					else:
						var['passworderror']="Password error"

				except:
					var['nameerror']='No such user!'
		else:
			var['loginForm'] = LoginForm()

		return render_to_response("login.html",
				var,
				context_instance=RequestContext(request))


def index(request):
	var = varInit(0)
	userChoice(request, var)
	return render_to_response('index.html', var)

def logout(request):
	if request.session.get('has_login'):
		del request.session['has_login']
		if request.session.get('name'):
			del request.session['name']
		return redirect("/login/") 
	else:
		return redirect("/login/") 

