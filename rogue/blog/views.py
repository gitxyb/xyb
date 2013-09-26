from django.contrib.auth.models import User
from blog.models import *
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import hashlib
import json

def user_regist(req):
	if req.method == "POST":
		username = req.POST['username']
		nickname = req.POST['nickname']
		password = req.POST['password']
		email  = req.POST['email']
		birthday = req.POST['birthday']
		sex = req.POST['sex']
		headImg = req.FILES['headimg']
		
		user = User.objects.create_user(username=username,first_name=nickname,password=password,email=email)
		ProUser.objects.create(user=user,birthday=birthday,sex=sex,headImg=headImg)
		return HttpResponseRedirect('/index/')
	return render(req,'regist.html',{})

def user_login(req):
	username = req.GET.get('username')
	password = req.GET.get('password')

	user = authenticate(username=username,password=password)
	if user is not None:
		login(req,user)
		responseJson = json.dumps({'username':user.first_name,'userid':user.id})
		return HttpResponse(responseJson)
	else:
		return HttpResponse('')

def user_logout(req):
	logout(req)
	return HttpResponseRedirect('/index/')


def post(req,id):
	posts = Post.objects.order_by('-id').all()
	paginator = Paginator(posts,6)
	page = req.GET.get('page')
	try:
		sends = paginator.page(page)
	except PageNotAnInteger:
		sends = paginator.page(1)
	except EmptyPage:
		sends = paginator.page(paginator.num_pages)
	if req.user.is_authenticated:
		if req.method == "POST":
			img = req.FILES['img']
			title = req.POST['title']
			content = req.POST['content']

			a = User.objects.get(id=id)
			Post.objects.create(user=a,img=img,title=title,content=content)
			return HttpResponseRedirect('/post_show/%s' % id)
	return render(req,'post.html',{'posts':sends})

def post_show(req,id):
	posts = Post.objects.order_by('-id').all()
	paginator = Paginator(posts,6)
	page = req.GET.get('page')
	try:
		sends = paginator.page(page)
	except PageNotAnInteger:
		sends = paginator.page(1)
	except EmptyPage:
		sends = paginator.page(paginator.num_pages)
	u = User.objects.get(id=id)
	post = u.post_set.order_by('-id').all()
	paginator = Paginator(post,3)
	page = req.GET.get('page')
	try:
		send = paginator.page(page)
	except PageNotAnInteger:
		send = paginator.page(1)
	except EmptyPage:
		send = paginator.page(paginator.num_pages)
	return render(req,'post_show.html',{'send':send,'posts':sends})

def replay(req,id):
	posts = Post.objects.order_by('-id').all()
	paginator = Paginator(posts,6)
	page = req.GET.get('page')
	try:
		sends = paginator.page(page)
	except PageNotAnInteger:
		sends = paginator.page(1)
	except EmptyPage:
		sends = paginator.page(paginator.num_pages)
	if req.user.is_authenticated:
		if req.method == "POST":
			content = req.POST['content']

			post = Post.objects.get(id=id)
			Replay.objects.create(user=req.user,post=post,content=content)
			return HttpResponseRedirect('/replay_show/%s' % id)
	return render(req,'replay.html',{'posts':sends})

def replay_show(req,id):
	posts = Post.objects.order_by('-id').all()
	paginator = Paginator(posts,6)
	page = req.GET.get('page')
	try:
		sends = paginator.page(page)
	except PageNotAnInteger:
		sends = paginator.page(1)
	except EmptyPage:
		sends = paginator.page(paginator.num_pages)
	p = Post.objects.get(id=id)
	replay = p.replay_set.order_by('-id').all()

	return render(req,'replay_show.html',{'send':replay,'p':p,'posts':sends})


def index(req):
	posts = Post.objects.order_by('-id').all()
	paginator = Paginator(posts,6)
	page = req.GET.get('page')
	try:
		sends = paginator.page(page)
	except PageNotAnInteger:
		sends = paginator.page(1)
	except EmptyPage:
		sends = paginator.page(paginator.num_pages)
	if req.user.is_authenticated:
		return render(req,'index.html',{'posts':sends})

def replay_user_show(req,id):
	posts = Post.objects.order_by('-id').all()
	paginator = Paginator(posts,6)
	page = req.GET.get('page')
	try:
		sends = paginator.page(page)
	except PageNotAnInteger:
		sends = paginator.page(1)
	except EmptyPage:
		sends = paginator.page(paginator.num_pages)
	u = User.objects.get(id=id)
	r = u.replay_set.order_by('-id').all()

	return render(req,'replay_user_show.html',{'r':r,'posts':sends})


