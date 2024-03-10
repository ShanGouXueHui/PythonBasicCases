from django.shortcuts import render
from django.shortcuts import redirect
from . import models


def index(request):
    #local()是Python中的一个内置函数，它可以将函数中的局部变量以字典的形式返回。
    #生产环境中，需要显示指定哪些变量值返回，否则可能会造成数据泄露  
    return render(request, 'index.html', locals())

def login(request):
    #如果用户已经登录，则直接跳转
    if request.session.get('isLogin', None):
        return redirect('/index/')
    if request.method == 'POST':
        username = request.POST.get('username')
        #生产环境中密码需要加密，为了主线简介，本例子暂不演示
        password = request.POST.get('password')
                
        #如果用户名和密码不为空，真实场景可以增加更多格式验证。
        message = '用户或密码错误，请输入正确的信息！'
        if username.strip() and password:
            try:
                #通过models查询数据库，免写sql语句，使用对象访问即可
                user = models.Users.objects.get(username=username)
                if user.password == password:
                    #登录成功后在session字典内写入用户状态；session里面写任何数据，不仅仅限于用户相关！
                    request.session['isLogin'] = True
                    return redirect('/index/')
                else:
                    return render(request, 'login.html', {'message': message})
            except:                
                return render(request, 'login.html', {'message': message})
        else:
            return render(request, 'login.html', {'message': message})
    return render(request,'login.html')

def register(request):
    #如果用户已经登录，则直接跳转
    if request.session.get('isLogin', None):
        return redirect('/index/')
    
    message = '请检查输入数据，是否合适！'
    if request.method == 'POST':
        username = request.POST.get('username')
        #生产环境中密码需要加密，为了主线简介，本例子暂不演示
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        #生产环境中数据需要判断格式，一般使用正则表达式完成，本例子暂不赘述
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        user = ''
        if username.strip() and password1 and (password1 == password2):
            try:
                #通过models查询数据库，免写sql语句，使用对象访问即可
                user = models.Users.objects.get(username=username)
            except:                
                pass
            
            if user:
                message = '用户名已存在，请重新输入'
                return render(request, 'register.html', {'message': message})
            else:
                #通过models模版将数据写入数据库，可以避免sql，直接用对象做操作
                newUser = models.Users()
                newUser.username = username
                newUser.password = password1
                newUser.gender = gender
                newUser.mobile = mobile
                newUser.save()
                #注册成功后，转入登录界面
                return redirect('/')
        else:
            return render(request, 'register.html', {'message': message})
    #local()是Python中的一个内置函数，它可以将函数中的局部变量以字典的形式返回。
    #生产环境中，需要显示指定哪些变量值返回，否则可能会造成数据泄露  
    return render(request, 'register.html', locals())
    

def logout(request):
    print(index, 'logout--------------------')
    #如果用户已登录，则清空session，否则直接跳转
    if request.session.get('isLogin', True):
        request.session.flush()
    return redirect('/')

    # username = models.CharField(max_length = 666)
    # password = models.CharField(max_length= 666)
    # mobile = models.CharField(max_length = 666)
    # gender = models.CharField(max_length = 8)
    # registerTime = models.DateTimeField(auto_now_add = True)
