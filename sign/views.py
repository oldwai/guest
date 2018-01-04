from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.context_processors import csrf

from sign.models import Event, Guest


def index(request):
    return render(request,"index.html",csrf(request))

def isli(request):
    return render(request,'isli.html')
    #pass

@login_required
def login_action(request):
    #return HttpResponse("哈哈哈哈哈登录成功了")
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,3600) #添加浏览器cookie
            request.session['user'] = username #将session信息记录到浏览器
            return response
        else:
            return render(request,"index.html",{'error':'username or password error!'})

@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response

@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','') #读取浏览器的cookie
    event_list = Event.objects.all()
    username = request.session.get('user','')  #读取浏览器的session
    return render(request,'event_manage.html',{'user':username,'events':event_list})

@login_required
def guest_manage(request):
    #username = request.COOKIES.get('user','') #读取浏览器的cookie
    username = request.session.get('user','')  #读取浏览器的session
    guest_list = Guest.objects.all()
    #设置每页显示数据的条数
    paginator_num = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator_num.page(page)
    except PageNotAnInteger:
        contacts = paginator_num.page(1)
    except EmptyPage:
        contacts = paginator_num.page(paginator_num.num_pages)

    return render(request,'guest_manage.html',{'user':username,'guests':contacts,})


@login_required
def search_name(request):
    username = request.session.get('user','')  #读取浏览器的session
    search_name= request.GET.get('name','')
    event_list= Event.objects.filter(name__contains=search_name)
    return render(request,'event_manage.html',{'user':username,'events':event_list})

@login_required
def sign_index(request,eid):
    event = get_object_or_404(Event, id = eid)
    return render(request,"sign_index.html",{'event':event})

@login_required
def sign_index_action(request,eid):
    event = get_object_or_404(Event, id = eid)
    phone = request.POST.get('phone','')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'输入的手机号错误.'})

    result = Guest.objects.filter(phone=phone,event_id=eid)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'与用户绑定的手机号不一致.'})

    result = Guest.objects.get(phone=phone,event_id=eid)
    if result.sign:
        return render(request,'sign_index.html',{'event':event,'hint':'用户已签到.'})
    else:
        Guest.objects.filter(phone=phone,event_id=eid).update(sign='1')
        return render(request,'sign_index.html',{'event':event,'hint':'签到成功','guest':result})


