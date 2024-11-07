from datetime import datetime
import io
import json
import os
import uuid
import shutil
import zipfile   
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from requests import Response

from api.search_engine import find_minzdrav_info
from fullstack.forms import RegisterForm, LoginForm
from utils.docx_utils import replace_tokens_in_docx


def index(request):
    login_form = RegisterForm()
    register_form = LoginForm()
    
    return render(request, "fullstack/auth.html", context={"login_form": login_form, "register_form": register_form})


def login_p(request):
    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("круто!")
        redirect("profile/")
        
        return HttpResponse("123")
    else:
        # Return an 'invalid login' error message.
        print("не вышло")
        return "Не вышло сори"


def register(request):
    pass


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect(f"/")
    
    return render(request, "fullstack/profile.html")


def search_inn(request):
    inn = request.POST["inn"]
    
    company_info = find_minzdrav_info(str(inn))
    
    if company_info == None:
        return HttpResponse(status=404)
    
    return HttpResponse(json.dumps(company_info), content_type="application/json")

def download_files(request):
    com_name = request.POST["company_name"]
    com_oid = request.POST["company_name"]
    
    date = datetime.now().strftime("%d.%m.%Y")
    
    token_pairs = {
        "{med_oid}": com_oid,
        "{med_name}": com_name,
        "{doc_date}": date,
    }
    
    ramd_doc = replace_tokens_in_docx("doc_templates/Template_RAMD.docx", token_pairs)
    iamk_doc = replace_tokens_in_docx("doc_templates/Template_IAMK.docx", token_pairs)

    user_dir = str(uuid.uuid4())
    ramd_doc_filename = f"{user_dir}/{uuid.uuid4()}.docx"
    iamk_doc_filename = f"{user_dir}/{uuid.uuid4()}.docx"
    
    os.mkdir(f"user_files/{user_dir}")
    
    ramd_doc.save(ramd_doc_filename)
    iamk_doc.save(iamk_doc_filename)
    
    
    shutil.make_archive(f"files_{str(uuid.uuid4())[:6]}", 'zip', f"user_files/{user_dir}")
    
    with open(f"files_{str(uuid.uuid4())[:6]}.zip", "rb") as f:
        response = HttpResponse(io.BytesIO(f.read()))
        response['Content-Type'] = 'application/x-zip-compressed'
        response['Content-Disposition'] = 'attachment; filename=album.zip'
    
    return response
    
    
    