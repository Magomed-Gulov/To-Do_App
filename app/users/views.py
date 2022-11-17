from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import authenticate, login


from .forms import RegistrationForm
from django.contrib.auth.models import User


# Create your views here.

def register(request):

    if request.method == 'POST':
        form = RegistrationForm( request.POST )

        username   = request.POST['username']
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        email      = request.POST['email']
        password   = request.POST['password']

        print( username, email, password )
        
        print( 0 )
        if len( User.objects.filter( Q( email__icontains=email ) ) ) == 0:
            print( 1 )
            user = authenticate(username='john', password='secret')

            # user = authenticate(
            #     # request,
            #     username=username,
            #     # first_name=first_name,
            #     # last_name=last_name,
            #     # email=email,
            #     password=password,
            # )
            
            # if user is not None:
            print( 2 )
            login( request, user )

                # return HttpResponseRedirect( '/todoapp/' )
            
            # else:
            #     return HttpResponseRedirect( '/user/register/' )

    else:

        form = RegistrationForm(  )

    context = {
        'form' : form,
    }

    return render( request, 'users/register.html', context )