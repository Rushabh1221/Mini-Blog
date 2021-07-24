from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import SignupForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group 
from django.contrib.auth.decorators import login_required


#For HomePage:
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})


#For AboutPage: 
def about(request): 
    return render(request, 'blog/about.html')     


#For ContactPage:
def contact(request):
    return render(request, 'blog/contact.html') 


#For DashboardPage:
@login_required
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all() 
        user = request.user
        full_name = user.get_full_name()
        grp = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':grp})
    else:
        return HttpResponseRedirect('/login/')   


#For Logout:
def ulogout(request):
    logout(request) 
    return HttpResponseRedirect('/')


#For SignupPage:
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congo!! Now You are an Author :)')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:        
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form':form})


#For LoginPage:
def ulogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You are logged in Successfully!! :)')
                    return HttpResponseRedirect('/dashboard/')
        else:                  
            form = LoginForm() 
        return render(request, 'blog/login.html', {'form':form}) 
    else:
        return HttpResponseRedirect('/dashboard/')



#For Liking the Post:
@login_required
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('post_id')) 
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.like_count -= 1
            result = post.like_count
            post.save()
        else:
            post.likes.add(request.user)
            post.like_count += 1
            result = post.like_count
            post.save()   

        return JsonResponse({'result':result})    



#For Adding New Post:
def addp(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid:
                messages.success(request, 'Your Post is Added!! :)')
                form.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addp.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')


#For Updating Exist Post:
def editp(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                messages.success(request, 'Post is updated!! :)')
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)                    
        return render(request, 'blog/editp.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')


#For Searching Post:
def searchpost(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
    return render(request, 'blog/searchp.html', {'posts':posts, 'searched':searched})

#For Deleting Post:
def deletep(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else: 
        return HttpResponseRedirect('/login/')    