from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.

#需要登陆才可以
@login_required
def profile_view(request):
    return render(request,'myauth/user_profile.html')

@login_required
def update_profile_view(request):
    if request.method == 'POST':
        # request.FILES  for upload files
        form = ProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('myauth:profile_url')
    else:
        # POST
        form = ProfileForm(instance = request.user)
    return render(request,'myauth/update_profile.html',context={'form':form})

