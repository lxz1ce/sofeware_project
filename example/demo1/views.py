import os

from django.shortcuts import render
from django.shortcuts import redirect
from demo1 import models, email as E
from django.shortcuts import get_object_or_404
def home(request):
	login_name = ''
	if request.session.get('id'):
		user = models.User.objects.get(id = request.session.get('id'))
		login_name = user.username
	return render(request, 'home.html', {"name": login_name})
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
				user = models.User.objects.get(username = username)
			except:
				message = '该用户名不存在'
				return render(request, 'login.html', {"message":message})
			if user.status == 0:
				message = '该用户尚未验证邮箱'
				return render(request, 'login.html', {"message": message})
			if user.password == password:
				request.session['id'] = user.id
				message = '登陆成功，欢迎您，' + str(user.username)
				return render(request, 'main.html', {"message": message})			#登录成功
			else:
				message = '密码错误'
				return render(request, 'login.html', {"message":message})
		else:
			message = '请输入用户名和密码'
			return render(request, 'login.html', {"message":message})
	return render(request, 'login.html')
def register(request):
	if request.session.get('id') != None:  # 只有不在登录状态时才可以进行注册
		return redirect('/')
	if request.method == 'POST':
		username = request.POST.get('username')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		email = request.POST.get('email')
		username = username.strip()  # 除去空格和换行
		password1 = password1.strip()
		password2 = password2.strip()
		email = email.strip()
		if models.User.objects.filter(username = username).exists():
			message = '该用户名已被注册'
			return render(request, 'register.html', {"message": message})
		elif models.User.objects.filter(email = email).exists() and models.User.objects.get(email = email).status == 1:
			message = '该邮箱已被注册'
			return render(request, 'register.html', {"message": message})
		elif password1 != password2:
			message = '两次密码不一致'
			return render(request, 'register.html', {"message": message})
		user = models.User()
		user.username = username
		user.password = password1
		user.email = email
		user.status = 0
		user.active_code = E.send_register_email(email)
		print(user.active_code)
		user.save()
		return redirect('/')
	return render(request, 'register.html')
def logout(request):
	request.session.flush()
	return redirect('/')
def active(request, active_code):
	all_users =	models.User.objects.filter(active_code = active_code)
	print(active_code)
	if all_users:
		for user in all_users:
			user.status = 1;
			user.save();
		message = '邮箱验证成功, 点击确认转到登录界面'
		return render(request, 'login.html', {"message": message})
	else:
		message = '邮箱验证失败，请重新注册'
		return render(request, 'register.html', {"message": message})
def main(request):
	if request.session.get('id') == None:
		return redirect('/')
	user = models.User.objects.get(id=request.session.get('id'))
	login_name = user.username
	return render(request, 'main.html', {"name": login_name})
def show_info(request):
	if request.session.get('id') == None:
		return redirect('/')
	return render(request, 'main.html')


def add_house(request):
	if request.method == 'POST':
		house_name = request.POST.get('house_name')
		short_leasing = request.POST.get('short_leasing')
		if short_leasing:
			short_leasing_fee = request.POST.get('short_leasing_fee')
		long_leasing = request.POST.get('long_leasing')
		if long_leasing:
			long_leasing_fee = request.POST.get('long_leasing_fee')
		house_type = request.POST.get('house_type')
		district = request.POST.get('district')
		address = request.POST.get('address')
		contact_number = request.POST.get('contact_number')
		file = request.FILES.get("photo", None)

		house = models.House()
		house.housename = house_name
		house.short_leasing = short_leasing
		if short_leasing :
			house.short_leasing_fee = short_leasing_fee
		house.long_leasing = long_leasing
		if long_leasing :
			house.long_leasing_fee = long_leasing_fee
		house.house_type = house_type
		house.district = district
		house.address = address
		house.contact_number = contact_number
		house.photo = file
		house.save()
		message = "添加成功"
		return render(request, 'add_house.html', locals())
	return render(request, 'add_house.html')


def search_house(request):
	houses = models.House.objects.all()
	if request.method == 'POST':
		key_word = request.POST.get('key_word')
		houses = models.House.objects.filter(housename__contains=key_word)
		short_leasing = request.POST.get('short_leasing')
		if short_leasing:
			houses = houses.filter(short_leasing=True)
		long_leasing = request.POST.get('long_leasing')
		if long_leasing:
			houses = houses.filter(long_leasing=True)
		houses = houses.filter(short_leasing_fee__gte=request.POST.get('short_min_fee'))
		houses = houses.filter(short_leasing_fee__lte=request.POST.get('short_max_fee'))
		houses = houses.filter(long_leasing_fee__gte=request.POST.get('long_min_fee'))
		houses = houses.filter(long_leasing_fee__lte=request.POST.get('long_max_fee'))
	return render(request, 'search_house.html', {'houses': houses})