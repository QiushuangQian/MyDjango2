from django.db import models

# Create your models here.

# 产品分类表
from django.db.models import Q, Sum, Count
from django.utils.html import format_html


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)

    # 设置返回值，若不设置则默认返回对象
    def __str__(self):
        return self.type_name


# 产品信息表
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'

    # 自定义函数，设置字体颜色
    def colored_type(self):
        if '手机' in self.type.type_name:
            color_code = 'red'
        elif '平板电脑' in self.type.type_name:
            color_code = 'blue'
        elif '智能穿戴' in self.type.type_name:
            color_code = 'green'
        else:
            color_code = 'yellow'
        return format_html(
            '<span style ="color:{}">{}</span>',
            color_code,
            self.type
        )

    colored_type.short_description = '带颜色的产品类型'


# 一对一关系，通过OneToOneField构建
'''
# class Performer(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20)
#     nationality = models.CharField(max_length=20)
#     masterpiece = models.CharField(max_length=50)

# class Performer_info(models.Model):
#     id = models.IntegerField(primary_key=True)
#     performer = models.OneToOneField(Performer, on_delete=models.CASCADE)
#     birth = models.CharField(max_length=20)
#     elapse = models.CharField(max_length=20)
'''

# 一对多关系，通过ForeignKey构建
'''
class Performer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

class Program(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
'''

# 多对多关系，通过ManyToManyField构建,只需写两个表，关系表会自动生成
'''
class Performer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

class Program(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.ManyToManyField(Performer)
    name = models.CharField(max_length=20)
'''

'''
# 数据插入，create()
Product.objects.create(name='荣耀V9', weight='110g', size='120*75*7mm', type_id=1)

# 数据更新，filter()进行筛选，update()进行更新
Product.objects.filter(name='荣耀V9').update(name='华为荣耀V9')

# 数据删除
# 删除表中全部数据
Product.objects.all().delete()
# 删除一条id为1的数据
Product.objects.get(id=1).delete()
# 删除多条数据
Product.objects.filter(name='华为荣耀V9')

# 数据查询
# 全表查询
Product.objects.all()
# 查询前五条
Product.objects.all()[:5]
# 查询某字段
Product.objects.values('name')
# 以列表方式返回数据，列表元素以元组表示
Product.objects.values_list('name')[:3]
# get方法查询，查询字段只能为主键或唯一约束字段
Product.objects.get(id=1)
# filter方法查询
Product.objects.filter(id=1)
# SQL中的and查询主要在filter中添加多个查询条件
Product.objects.filter(name='华为荣耀V9', id=1)
# SQL中的or查询需要引入Q，格式：Q(field=value)|Q(field=value)
# from django.db.models import Q
Product.objects.filter(Q(name='华为荣耀V9') | Q(id=1))
# 去重查询(根据values）
Product.objects.values('name').filter('华为荣耀V9').distinct()
# 降序查询
Product.objects.order_by('-id')
# 聚合查询，实现对数据的求和、求平均等
# annotate类似于GROUP BY，不设values则默认对主键操作
Product.objects.values('name').annotate(Sum('id'))
# aggregate是将某个字段的值进行计算并只返回计算结果
Product.objects.aggregate(id_count=Count('id'))

# 多表查询
# 设查询主体为Type
# 正向查询
Type.objects.filter(product__id=11)
# 反向查询
t = Type.objects.filter(product__id=11)
t[0].product_set.values('name')
'''
