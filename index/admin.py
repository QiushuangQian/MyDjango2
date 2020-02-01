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
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        else:
            self.readonly_fields = ['name']
        return self.readonly_fields

    # 设置Admin的标题
    list_display.append('colored_type')

    # 根据当前用户名设置数据访问权限
    def get_queryset(self, request):
        # 通过super方法获取父类ModelAdmin的函数get_queryset所生成的查询对象，该对象用于查询模型Product的全部数据类型
        qs = super(ProductAdmin, self).get_queryset(request)
        # 判断身份
        # 超级管理员则返回Product全部数据
        if request.user.is_superuser:
            return qs
        # 普通用户则返回Product的前5条数据
        else:
            return qs.filter(id__lt=6)

    # 新增或修改数据时，设置外键可选值
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # 设置外键对象
        if db_field.name == 'type':
            if not request.user.is_superuser:
                kwargs['queryset'] = Type.objects.filter(id__lt=4)
        return super(admin.ModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # 保存修改
    '''
    判断change是否为True，True则代表当前操作为数据修改，反之为新增数据
    分别从三个函数对象中获取相关的数据内容。request代表当前用户的请求对象，obj代表当前数据所对应的模型对象，
    form代表Admin的数据修改页所对应的数据表单
    super方法对数据进行入库和变更处理
    '''

    def save_model(self, request, obj, form, change):
        if change:
            # 获取当前用户名
            user = request.user
            # 使用模型获取数据，pk代表具有主键属性的字段
            name = self.model.objects.get(pk=obj.pk).name
            # 使用表单获取数据
            weight = form.cleaned_data['weight']
            # 写入日志
            # f = open('D://MyDjango_log.txt','a')
            # f.write('产品：'+str(name)+'，被用户：'+str(user)+' 修改'+'\r\n')
            # f.close()
        else:
            pass
        # super可使自定义save_model既保留父类已有的功能又添加自定义的功能
        super(ProductAdmin, self).save_model(request, obj, form, change)

    # 删除数据
    def delete_model(self, request, obj):
        pass
        super(ProductAdmin, self).delete_model(request, obj)
