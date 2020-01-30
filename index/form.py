from django import forms
from .models import *
from django.core.exceptions import ValidationError

'''
内置表单字段：
BooleanField：复选框
CharField：文本框
ChoiceField：下拉框
TypedChoiceField：加强版下拉框，多出参数coerce(强制转换数据类型)和empty_value(表示空值)
DateField：文本框，验证日期功能，参数input_formats设置日期格式
EmailField：文本框，验证输入数据是否为合法邮箱，参数：max_length/min_length
FileField：文件上传功能，参数max_length/allow_empty_file
FilePathField：在特定目录选择并上传文件，path必需，recursive、match、allow_files、allow_folders可选
FloatField：验证数据是否为浮点数
ImageField：验证文件是否为可识别的图像格式
GenericIPAddressField：验证数据是否为有效数值
SlugField：验证数据是否只包括字母、数字、下划线及连字符
TimeField：验证数据是否为datetime.time或指定特定时间格式的字符串
URLField：验证数据是否为有效URL地址
'''

'''
共同参数：
Required：输入是否为空，默认True
Widget：设置HTML控件样式
Label：生成Label标签或显示内容
Initial：设初值
help_text：设置帮助提示信息
error_messages：设置错误信息，以字典形式表示：{'required':'不能为空','invalid':'格式错误'}
show_hidden_initial：值为True/False，是否在当前插件后面再加一个隐藏的且具有默认值的插件（检验两次输入值是否一致）
Validators：自定义数据验证规则。以list格式表示，list元素为函数名
Localize：值为True/False，是否支持本地化（不同时区显示相应的时间）
Disabled：值为True/False，是否可以编辑
label_suffix：Label内容后缀，在Label后添加内容
'''


def weight_validate(value):
    if not str(value).isdigit():
        raise ValidationError('请输入正确的重量')


class ProductForm(forms.Form):
    # 设置错误信息并设置样式
    name = forms.CharField(max_length=20, label='名字', widget=forms.widgets.TextInput(attrs={'class': 'c1'}),
                           error_messages={'required': '名字不能为空'})
    weight = forms.CharField(max_length=20, label='重量', validators=[weight_validate])
    size = forms.CharField(max_length=50, label='尺寸')

    # 下拉框
    choices_list = [(i + 1, v['type_name']) for i, v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class': 'type', 'size': '4'}), choices=choices_list,
                             label='产品类型')

class ProductModelForm(forms.ModelForm):
    # 添加模型外的表单字段
    productId = forms.CharField(max_length=20, label='产品序号')

    # 类Meta的属性说明
    # model：必需属性，绑定Model对象
    # fields：必须属性，设置哪些字段转换成表单字段
    # exclude：可选属性，禁止哪些字段转换成表单字段
    # labels：可选属性，设置表单字段的参数label
    # widgets：可选属性，设置表单字段的参数widget
    # field_classes：可选属性，将模型的字段类型重新定义为表单字段类型
    # help_texts：可选属性，设置表单字段的参数help_text
    # error_messages：可选属性，设置表单字段的参数error_messages
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

    # 自定义表单字段weight的数据清洗
    def clean_weight(self):
        # 获取数据
        data = self.cleaned_data['weight']
        return data + 'g'
