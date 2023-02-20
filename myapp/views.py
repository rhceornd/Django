from django.shortcuts import render, HttpResponse

# Create your views here.
# 클라이언트로 정보를 전달하는 함수
def index(request):
    return HttpResponse("Welcome") # reponse through http

def create(request):
    return HttpResponse("Create")

def read(request, id):
    return HttpResponse("Read!" + id)