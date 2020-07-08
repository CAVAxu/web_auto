from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def navigationList(request):
    name_list = [
        {
        "type": "词典",
        "value": ["汉语词典", "英语词典", "英汉词典"]
        },
        {
        "type": "语音检索",
        "value": ["语文", "数学", "英语"]
        },
        {
        "type": "不一样的开学季",
        "value": ["小学", "初中", "高中"]
        },        {
        "type": "不一样的开学季",
        "value": []
        }
    ]
    context = {"nav_name": name_list}
    return render(request, "navlist.html", context=context)


def personInfo(request):
    class myBlog():
        def __init__(self):
            self.name = "bingo"
            self.age = 20
        def guanzhu(self):
            return 200
        def fans(self):
            return 2000
    #实例化
    myblog = myBlog()

    info = {
        "nicheng": "bingo_x",
        "age": 20,
        "fancy": ["python", "basketball", "shopping"],
        "blog": {
            "url": "https://www.cnblogs.com/cavaXu/",
            "img": "https://images2018.cnblogs.com/blog/1208861/201803/1208861-20180328150854275-1833485454.png"
            },
        "MyBlog": myblog
        }
    # info["MyBlog"] = myblog

    return render(request, "personinfo.html", info)

def register(request):
    return render(request, "register.html", {"year": "2020-06-30"})

def archive(request, year, month):
    res = {
    "code": 0,
    "msg": "获取succsss!",
    "data": [
        {"year":year},
        {"month":month}
    ]
}
    return JsonResponse(res,
                        json_dumps_params={'ensure_ascii':False})

def hello(request):
    # return HttpResponse("hello world!!!")
    res = {
        "code":"200",
        "msg":"访问成功！",
        "data":["user","psw"]
    }
    return JsonResponse(res,
                        json_dumps_params={'ensure_ascii':False})    #显示中文

def login(request):
    return render(request,"login.html")