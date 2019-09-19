# coding=utf-8
from django.http import HttpResponse
from pf.models import *

def dbinsert(request):
	test1	= Test(name=request.GET["name"]);
	test1.save();
	return HttpResponse('测试添加数据成功');
	
def dbselect(request):
	# 初始化
	response	= '';
	response1	= '';
	
	#通过objects模拟管理器的all 获取所有数据
	list		= Test.objects.all();
	#通过 filter 过滤
	response2	= Test.objects.get(id=1);
	response3	= Test.objects.filter(name='34');
	# limit 限制
	response4	= Test.objects.order_by('name')[0:2];
	
	# 查询构造器使用
	response5	= Test.objects.filter(name="runoob").order_by('id')[0:1];
	
	for v in response3:
		response1 +=v.name+',';
		
	
		
	return HttpResponse(response2.memo);
	
	
	
def dbupdate(request):
	# orm	= Test.objects.get(id=2);
	# orm.memo='update';
	# orm.save();
	
	Test.objects.filter(name='runoob').update(memo='update3');
	
	return HttpResponse('update success...');
	
	
def dbdelete(request):
	test	= Test.objects.get(id=7);
	test.delete();
	return HttpResponse('dbdelete success...');