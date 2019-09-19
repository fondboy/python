# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.views.decorators import csrf

# 视图渲染
def test(request):
	context	= {}
	context['hello']	= '这是helloword 视图模板渲染';
	#print(BASE_DIR)
	return render(request,'helloword.html',context);

# 表单
def searchForm(request):
	return render(request,'search_form.html'); 
	return render_to_response('search_form.html');
	
	#return render_to_response('search_form.html');

# 搜索动作	
def doSearch(request):
	request.encoding='utf-8'
	if request.POST['q']:
		message = '你搜索的内容为: ' + request.POST['q']
	else:
		message = '你提交了空表单'

	return HttpResponse(u'a:'+request.method+message+request.path);