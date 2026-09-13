import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from hobbies.forms import InputForm
from hobbies.models import Users
oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )
def debug(request):
    user =Users(userid='google-oauth2|000000000000000000004',fname='Billy',lname="Bob", age= 42, username= 'bobbyjoe', bio= 'yeehaw', city= 'Lubbock')
    #user.save()
    return render(
        request,
        "debug.html",
        context={
            "data":Users.objects.all().values()
        }
    )
def home(request):
    print(json.dumps(request.session.get("user"), indent=4))
    f=InputForm(request.POST or None)
    if f.is_valid():
        nu=f.save(commit=False)
        nu.userid=request.session.get("user")["userinfo"]["sub"]
        nu.save()
        f.save_m2m()

    return render(
        request,
        "home.html",
        context={
            "uidexists":not Users.objects.filter(userid=(request.session.get("user")["userinfo"]["sub"] if request.session.get("user")!=None else "")),
            "form":f,
            "session": request.session.get("user")
        }
    )

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("home")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("home")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )
def matchfindr(request):
    return render(
        request,
        "MatchFindr.html",
        context={
            "session":request.session.get("user"),
        }
    )