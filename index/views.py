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


class ProductModelForm(forms.ModelForm):
    # 添加模型外的表单字段
    productId = forms.CharField(max_length=20, label='产品序号')

    # 模型与表单设置
    class Meta:
        # 绑定模型
        model = Product
        # fields属性用于设置转换字段，'_all_'是将全部模型字段转换成表单字段
        # fields= '_all_'
        fields = ['name', 'weight', 'size', 'type']
        # exclude用于禁止模型字段转换表单字段
        exclude = []
        # label设置HTML元素控件的label标签
        labels = {
            'name': '产品名称',
            'weight': '重量',
            'size': '尺寸',
            'type': '产品类型'
        }
        # 定义widgets,设置表单字段的css模式
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'c1'})
        }

        # 定义字段的类型
        field_classes = {
            'name': forms.CharField
        }
        # 帮助提示信息
        help_texts = {
            'name': ''
        }
        # 自定义错误信息
        error_messages = {
            # _all_设置全部错误信息
            '_all_': {'required': '请输入内容', 'invalid': '请检查输入内容'},
            # 设置某字段
            'weight': {'required': '请输入重量数值', 'invalid': '请检查数值是否正确'}
        }

    def clean_weight(self):
        data = self.cleaned_data['weight']
        return data + 'g'
