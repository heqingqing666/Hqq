from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        print(uname, pwd)
        if uname == 'hqq' and pwd == '123':
            print('登入成功')
            # return redirect('/test/')
            return redirect('/app01/test/',)
        else:
            return HttpResponse('登入失败')


def app01(request):
    return HttpResponse('app01的首页')


def test(request):
    return render(request, 'test.html')


def test1(request):
    if request.method == "GET":
        return render(request, "test1.html")
    else:
        print(request.POST.get('name'))
        # return redirect('/test/')
        return render(request, "test.html")
