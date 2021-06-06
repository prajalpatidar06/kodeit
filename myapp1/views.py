from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Blog
from . forms import Edit_Blog
# Create your views here.

def index(request):
    blog = Blog.objects.all()
    context = {'blogs': blog}
    return render(request,'home.html',context)

def user_view(request):
    blogs = Blog.objects.all()
    count = 0
    for blog in blogs:
        if blog.user_id == request.user:
            count += 1
    context = {'blogs': blogs , 'count': count}
    return render(request,'user_view.html' , context)

def user_register(request):
    if request.method =='POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.warning(request,"Password does not match")
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'Username already exist , please try different username')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'E-mail already exist , please try different email')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name = fname,last_name = lname,username = uname,email = email,password = pass1)
            user.save()
            messages.success(request,'Succesfully registered')
            return redirect('_login')
    
    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'Incorrect username or password , please try again')
            return redirect('_login')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def post_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        category2 = request.POST.get('category_new')
        url = request.POST.get('url')
        description = request.POST.get('description')
        if category  != 'none':
            blog = Blog(title=title, category=category, url=url, description=description , user_id = request.user)
            blog.save()
        elif category2 != '':
            blog = Blog(title=title, category=category2, url=url, description=description , user_id = request.user)
            blog.save()
        
        messages.success(request,'Blog content successfully posted')
        return redirect('post_blog')
    blog = Blog.objects.all()  
    return render(request,'post_blog.html',{'blogs':blog})

def blog_detail(request,id):
    blog = Blog.objects.get(id =id)
    context = {'blog':blog}
    return render(request,'blog_detail.html',context)

def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request,'Blog has been Deleted')
    return redirect('/')

def edit(request,id):
    blog = Blog.objects.get(id=id)
    post = Blog.objects.all()
    editblog = Edit_Blog(instance = blog)
    if request.method =="POST":
        form = Edit_Blog(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,'Blog has been Edited')
            return redirect('/')
    return render(request,'edit_blog.html',{'edit_blog' :editblog , 'posts':post})

def search(request):
    query = request.GET.get('search')
    blog= Blog.objects.all()
    return render(request,'search.html',{'blogs':blog , 'query' :query})
