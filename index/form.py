from django import forms
from .models import *
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
Validators：自定义数据验证规则。以列表格式表示，列表元素为函数名
Localize：值为True/False，是否支持本地化（不同时区显示相应的时间）
Disabled：值为True/False，是否可以编辑
label_suffix：Label内容后缀，在Label后添加内容
'''
class ProductForm(forms.Form):
    name = forms.CharField(max_length=20,label='名字')
    weight = forms.CharField(max_length=20,label='重量')
    size = forms.CharField(max_length=50,label='尺寸')

    #下拉框
    choices_list = [(i+1,v['type_name']) for i,v in enumerate(Type.objects.values('type_name'))]
    type =forms.ChoiceField(choices=choices_list,label='产品类型')