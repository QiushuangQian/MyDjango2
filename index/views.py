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


def models_index(request, id):
    if request.method == 'GET':
        instance = Product.objects.filter(id=id)
        # 判断数据是否存在
        if instance:
            product = ProductModelForm(instance=instance[0])
        else:
            product = ProductModelForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            # 获取weight的数据
            weight = product.cleaned_data['weight']
            # 数据保存方法
            # 方法一：直接保存到数据库
            # product.save()
            # 方法二：save方法设置commit=False，将生成数据库对象product_db，然后对该对象的属性值修改并保存
            product_db = product.save(commit=False)
            product_db.name = '我的IPhone'
            product_db.save()
            # 方法三：save_m2m()用于保存ManyToMany的数据模型
            # product.save_m2m:()
            return HttpResponse('提交成功！weight清洗后的数据为：' + weight)
        else:
            # 输出错误信息
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())
