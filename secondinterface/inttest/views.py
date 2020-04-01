#coding=utf8
from django.shortcuts import render
from django.http import response,HttpResponse,JsonResponse
from .models import InterTest,Cars,Person
from django.views.decorators.csrf import csrf_exempt
from .func import param_handle,getkeys
from django.shortcuts import redirect
import json,requests
#胆大心细脸皮厚

#新增数据
def add(request):
    a=InterTest(name='接口1',method='get',url='127.0.0.1',intername='index')
    a.save()
    return HttpResponse('ok')
#查询数据
def query(request):
    b=InterTest.objects.all()
    print(b.values())
    print(b.values_list())
    return HttpResponse('dd')
#删除数据
def delete(request):
    c=InterTest.objects.get(pid=2)
    c.delete()
    return HttpResponse('删除成功')
#更改数据
def change(request):
    d=InterTest.objects.get(pid=1)
    d.name="接口2"
    d.intername='change'
    d.save()
    return HttpResponse(d.intername)
#接口页面首页
def interface(request):
    all_inter=InterTest.objects.values()
    return render(request,"interface.html",{'interlist':all_inter})
def loadall(request):
    all_inter=InterTest.objects.values()
    print(all_inter)
    return HttpResponse("ok")
def cars(request):
    name=request.GET.get('name')
    c=Cars.objects.values()
    l=Cars.objects.values().get(name=name)
    #objects.values()返回全部数据，类型queryset
    #objects.values().get(name=name)条件查询，返回list,不能list()方法
    #objects.values().filter(name=name)与get方法一样，不过返回queryset
    print(c,l)
    data = {}
    data['list'] = list(c)
    # dat=str(data)
    # da=json.loads(dat,encoding='utf8')
    # return HttpResponse(da)
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False})
@csrf_exempt
def compare(request):
    respon=json.loads(request.body,encoding='utf8')
    print(type(respon),respon)
    actual=eval(respon.get('actual'))  #实际结果，转换成字典
    print(type(actual),actual)
    expect=respon.get('expect')      #预期结果
    act=set(getkeys(actual))
    exp=set(expect.split('\n'))
    print(exp,act)
    #求集合的对称差集，即没有同时出现在两个集合中的元素。
    no_have=exp ^ act
    str_have=str(list(no_have))    #这里str方法，前段返回的是数组对象。
    return HttpResponse(str_have)
@csrf_exempt
def action(request):
    baseurl='http://127.0.0.1:8000/'
    data=request.POST
    reb=json.loads(request.body,encoding='utf8')

    print(data)
    print(reb)
    #处理提交的数据
    url=reb.get('sel').split('-')[1]
    param=reb.get('param','')
    params=param_handle(param)
    urls=baseurl+url
    re=requests.get(urls,params=params)
    return HttpResponse(re.content)



'''
遇到的问题：
post提交cfrs问题
ajax提交json数据
request.POST的问题：只有请求header中的'Content-Type'：'application/x-www-form-urlencoded'才会填充request.POST，其它情况下只有一个空的<QueryDict: {}>
request.body
'''