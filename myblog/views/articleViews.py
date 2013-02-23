#coding=utf-8
from django.shortcuts import render_to_response
from django.http import Http404
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from myblog.models import *
from basic import *
import re
import datetime
from myblog.forms import *

def cat(request, id):
	var = varInit(1)
	userChoice(request, var)
	try:
		category = Category.objects.get(id=id)
	except:
		raise Http404
	if category:
		articles = Blog.objects.filter(category = category)
		var['articles'] = articles
		var['categorys'] = []
		categorys = Category.objects.all()
		for category in categorys:
			var['categorys'].append({
				'count':Blog.objects.filter(category = category).count(),
				'info':category
				})
		return render_to_response("article.html", var)



def article(request):
	var = varInit(1)
	userChoice(request, var)
	articles = Blog.objects.order_by('publish_time')[0:10]
	var['articles'] = articles
	var['categorys'] = []
	categorys = Category.objects.all()
	for category in categorys:
		var['categorys'].append({
			'count':Blog.objects.filter(category = category).count(),
			'info':category
			})
	return render_to_response("article.html", var)


def addarticle(request):
	var = varInit(1)
	userChoice(request, var)
	if request.method == 'POST':
		var['form'] = BlogForm(request.POST)
		if var['form'].is_valid():
			cd_form = var['form'].cleaned_data
			title = cd_form['caption']
			author = User.objects.get(name=request.session['name'])
			content = cd_form['content']

			category = cd_form['category']
			Category.objects.get_or_create(name = category)
			c1 = Category.objects.get(name = category)
			blog = Blog(caption=title, author=author, content=content, category = c1)
			tagname = cd_form['tag_name']
			for taglist in tagname.split(' '):
				Tag.objects.get_or_create(tag_name=taglist.strip())
			blog.save()
			for taglist in tagname.split(' '):
				blog.tags.add(Tag.objects.get(tag_name = taglist.strip()))
				blog.save()
			return redirect('/article/')
	else:
		var['categorys'] = Category.objects.all()
		var['form'] = BlogForm(initial={'category':'未分类类别'})
	return render_to_response("addarticle.html",
					var,
					context_instance=RequestContext(request))


def deleteblog(request):
	var = varInit(1)
	userChoice(request, var)
	if request.method =='GET':
		if 'id' in request.GET:
			id = request.GET['id']
			try:
				blog = Blog.objects.get(id=id)
			except:
				raise Http404
			if blog:
				blog.delete()
				return redirect('/article/')
	raise Http404

def modifyblog(request):
	var = varInit(1)
	userChoice(request, var)
	id = ''
	if 'id' in request.GET:
		id = request.GET['id']

	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			cd_form = form.cleaned_data
			taglist = cd_form['tag_name']
			tagNameList = taglist.split(' ')
			for tag in tagNameList:
				Tag.objects.get_or_create(tag_name=tag.strip())
			title = cd_form['caption']
			content = cd_form['content']
			category = cd_form['category']
			blog = Blog.objects.get(id=id)
			if blog:
				blog.caption = title
				blog.content = content 
				blog.category = Category.objects.get(name=category)
				blog.save()
				alltag = blog.tags.all()
				for tag in alltag:
					tag= unicode(str(tag),"utf-8")
					if tag not in tagNameList:
						notag = blog.tags.get(tag_name=tag)
						blog.tags.remove(notag)

			return redirect("/article/")

	if request.method == 'GET':
			try:
				blog = Blog.objects.get(id=id)
			except:
				raise Http404
			if blog:
				tags = blog.tags.all()
				taglist = ''
				if tags:
					for tag in tags:
						taglist += str(tag) + " "
			form = BlogForm(initial={'caption': blog.caption, 'content':blog.content, 'tag_name':taglist,'category':blog.category} )
			var['form'] = form
			var['categorys'] = Category.objects.all()
			return render_to_response("addarticle.html",
					var,
					context_instance=RequestContext(request))


def showblog(request):
	var = varInit(1)
	userChoice(request, var)
	var['categorys'] = []
	categorys = Category.objects.all()
	for category in categorys:
		var['categorys'].append({
			'count':Blog.objects.filter(category = category).count(),
			'info':category
			})

	id = ''
	if 'id' in request.GET:
		id = request.GET['id']
		try:
			blog = Blog.objects.get(id=request.GET['id'])
		except:
			raise Http404
		if blog:
			var['article'] = blog
			var['comments'] = Comments.objects.filter(blog=blog)
			var['commentForm'] = CommentForm()
			
		if request.method == 'POST':
			commentForm = CommentForm(request.POST)
			var['commentForm'] = commentForm
			if commentForm.is_valid():
				cd_comment = commentForm.cleaned_data
				var['commentForm'] = CommentForm()
				comment = Comments(author = cd_comment['name'],
						email = cd_comment['email'],
						content = cd_comment['content'],
						blog = blog
						)
				comment.save()
		return render_to_response("showblog.html",
				var,
				context_instance=RequestContext(request))
	raise Http404

