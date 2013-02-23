#coding=utf-8

def checkPost(var, request):
	if not request.POST.get('name', ''):
		var['error'].append("Enter your name!")
		return False
	if not request.POST.get('password', ''):
		var['error'].append("Enter your password!")
		return False
	return True

def checkValidAddarticle(var, request):
	if not request.POST.get('title', ''):
		var['error'].append("请输入标题!")
		return False

	if not request.POST.get('content', ''):
		var['error'].append("正文不能为空!")
		return False
	return True

def varInit( active ):
	var = {}
	var['error'] = []
	var['info'] = []
	var['header'] = []
	for x in range(0, 2):
		if x == active:
			var['header'].append("active")
		else:
			var['header'].append("")
	return var;

def userChoice(request, var):
	var['userChoice'] = []
	if request.session.get('has_login'):
		var['myuser'] = {'name':request.session['name']+"的帐号".decode("utf-8"),
			'info': '#'
			}
		var['userChoice'].append({'name': "添加日志",
			'info': '/addarticle/'
			})
		var['userChoice'].append({'name': "退出",
			'info': '/logout/'
			})


		var['has_login'] = True

	else:
		var['myuser'] = {'name': "你好, 游客",
			'info': ''
			}
		var['userChoice'].append({'name': "登录",
			'info': '/login/'
			})
		var['userChoice'].append({'name': "注册",
			'info': '/registry/'
			})
		var['has_login'] = False




