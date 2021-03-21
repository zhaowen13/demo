# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class case(models.Model):
    name = models.CharField('用例名称', max_length=100)
    module = models.CharField('所属模块', max_length=100)
    step = models.CharField('操作步骤', max_length=1000)
    result = models.CharField('预期结果', max_length=1000)
    grade = models.CharField('用例等级', max_length=100)
    execution = models.CharField('执行状态', max_length=100)
    cover = models.CharField('覆盖状态', max_length=100)

    def __unicode__(self):
        return self.fundcode

    class Meta:
        db_table = "case"


class apicase(models.Model):
    name = models.CharField('case名称', help_text="case名称", max_length=64)
    method = models.CharField('请求方式', max_length=64)
    headers = models.CharField('headers', max_length=1000, null=True)
    body = models.CharField('body', max_length=5000, null=True)
    expected = models.CharField('预期结果', max_length=100)
    actual = models.CharField('实际结果', max_length=100)
    module_id = models.PositiveIntegerField('所属模块id', max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.fundcode

    class Meta:
        db_table = "apicase"


class module(models.Model):
    name = models.CharField('模块名', max_length=64)
    file_name = models.CharField('json文件名', max_length=64)
    project_id = models.PositiveSmallIntegerField('项目ID', max_length=11)

    def __unicode__(self):
        return self.fundcode

    class Meta:
        db_table = "module"
