from django.contrib import admin
from .models import *

# Register your models here.
'''
# 方法一：直接将模型注册到admin后台
admin.site.register(Product)
'''
# 修改title和header
admin.site.set_title = 'MyDjango后台管理'
admin.site.set_header = 'MyDjango'


# 方法二：自定义ProductAdmin类并继承ModelAdmin
# 注册方法一：使用Python装饰器将ProductAdmin和模型Product绑定并注册到后台
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 设置显示字段
    list_display = ['id', 'name', 'weight', 'size', 'type', ]
    # 注册方法二：
    # admin.site.register(Product,ProductAdmin)
    # 设置可搜索的字段并在Admin后台数据生成搜索框，如有外键，应使用双下划线连接两个模型的字段
    search_fields = ['id', 'name', 'type__type_name']
    # 设置过滤器，在后台数据的右侧生成导航栏，如有外键，应使用双下划线连接两个模型的字段
    list_filter = ['name', 'type__type_name']
    # 设置排序方式，['id']为升序，-id为降序
    ordering = ['id']
    # 设置时间选择器，如字段中由时间格式才可以使用
    # date_hierarchy = Field
    # 在添加新数据时，设置可添加数据的字段
    fields = ['name', 'weight', 'size', 'type']
    # 设置可读字段，在修改或者新增数据时使其无法设置
    readonly_fields = ['name']
