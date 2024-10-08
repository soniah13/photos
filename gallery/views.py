from django.shortcuts import render, redirect, get_object_or_404
from .forms import PicForm, DisplayForm
from .models import Picture
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout

# Create your views here.
@login_required(login_url = 'login_user')
def Home(request):
    category = request.GET.get('category', None)
    if category:
        pictures = Picture.objects.filter(tag_category=category)
    else:
        pictures = Picture.objects.all()
    return render(request, 'home.html', {'pictures': pictures})

@login_required(login_url = 'login_user')
def add_pic(request):
    if request.method == 'POST':
        add_form = PicForm(request.POST, request.FILES)
        if add_form.is_valid():
            picture = add_form.save(commit = False) # save the picture but not to database
            picture.user = request.user #assiciate that picture with specified user
            picture.save() # save to user's database
            add_form.save_m2m() #save form using many to many relation like(likes, tags)
            messages.success(request, 'Photo was uploaded successfully')
            return redirect('home')# redirect to home page
        else:
            messages.error(request, 'Error occured during upload, check form...')
    else:
        add_form = PicForm()
    return render(request, 'add_pic.html',
                      {'add_form': add_form})
    
@login_required(login_url = 'login_user')   
def pic_details(request, pic_id):
    pic = get_object_or_404(Picture, id=pic_id)
    detail_form = DisplayForm(instance=pic)
    if request.method == 'POST':
        if pic.id in request.session.get('pic_likes', []):
            request.session['pic_likes'].remove(pic.id)  # Remove if already liked
            messages.success(request, 'You unliked this picture.')
        else:
            request.session.setdefault('pic_likes', []).append(pic.id)  # Add to liked pictures
            messages.success(request, 'You liked this picture.')
        request.session.modified = True
    return render(request, 'pic_details.html', {'detail_form': detail_form, 'pic': pic})


def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login_user')
    context = {'registerform': form}
    return render(request, 'register_user.html', context=context)

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    context = {'loginform':form}
    return render(request, 'login_user.html', context=context)

def logout_user(request):
    auth_logout(request)
    return redirect('login_user')
    

    