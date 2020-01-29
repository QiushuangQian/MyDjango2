from django.db import models


# Create your models here.

# 产品分类表
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)


# 产品信息表
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)


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
