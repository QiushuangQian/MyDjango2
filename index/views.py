from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .form import *


def index(request):
    # product = ProductForm()
    # return render(request,'data_form.html',locals())
    if request.method == 'GET':
        product = ProductForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
            # 获取name的数据
            # 方法一：
            name = product['name']
            # 方法二：clean_data将控件name的数据进行清洗，转换为Python数据类型
            cname = product.cleaned_data['name']
            return HttpResponse('提交成功')
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())
