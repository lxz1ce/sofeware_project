from django.shortcuts import render
from django.shortcuts import redirect
from demo1 import models
# Create your views here.
def home(request):
	login_name = ''
	if request.session.get('id'):
		user = models.User.objects.get(id=request.session.get('id'))
		login_name = user.username
	return render(request, 'Home.html', {"name": login_name})
def login(request):
	if request.session.get('id') != None:
		return redirect('/')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username and password:
			username = username.strip()
			password = password.strip()
			try:
				user = models.User.objects.get(username=username)
			except:
				message = '该用户名不存在'
				return render(request, 'login.html', {"message":message})
			if user.password == password:
				request.session['id'] = user.id
				return redirect('/')
			else:
				massage = '密码错误'
				return render(request, 'login.html', {"message":message})
	return render(request, 'login.html')
def register(request):
	if request.session.get('id') != None:  # 只有不在登录状态时才可以进行注册
		return redirect('/')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		username = username.strip()  # 除去空格和换行
		password = password.strip()
		if models.User.objects.filter(username=username).exists():
			message = '该用户名已被注册'
			return render(request, 'Register.html', {"message": message})
		user = models.User()
		user.username = username
		user.password = password
		user.save()
		request.session['id'] = user.id  # 记录用户已登录
		return redirect('/')
	return render(request, 'register.html')
def logout(request):
	request.session.flush()
	return redirect('/')