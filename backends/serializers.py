# -*- coding: utf8 -*-
import logging

from rest_framework import serializers

from backends.models.main import RegionConfig
from www.models.main import Users

logger = logging.getLogger("default")


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'email', 'nick_name',)


class RegionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = RegionConfig
        fields = ("region_name", "region_alias", "url", "token", "status")


class NodeSerilizer(serializers.Serializer):
    host_name = serializers.CharField(max_length=32, required=True, help_text="host name")
    internal_ip = serializers.CharField(max_length=32, required=True, help_text="internal ip")
    external_ip = serializers.CharField(max_length=32, required=True, help_text="external ip")
    available_memory = serializers.IntegerField(help_text="可用内存")
    available_cpu = serializers.IntegerField(help_text="可用cpu")
    role = serializers.CharField(max_length=32, required=True, help_text="节点类型")
    status = serializers.CharField(max_length=32, required=False, help_text="状态")
    labels = serializers.JSONField(binary=False, required=True, help_text="标签")
    unschedulable = serializers.BooleanField(required=True, help_text="可否调度")


class NodeUpdateSerilizer(serializers.Serializer):
    host_name = serializers.CharField(max_length=32, required=False, help_text="host name")
    uuid = serializers.CharField(max_length=36, required=True, help_text="UUID标识")
    internal_ip = serializers.CharField(max_length=32, required=False, help_text="internal ip")
    external_ip = serializers.CharField(max_length=32, required=False, help_text="external ip")
    available_memory = serializers.IntegerField(required=False, help_text="可用内存")
    available_cpu = serializers.IntegerField(required=False, help_text="可用cpu")
    role = serializers.CharField(max_length=32, required=False, help_text="节点类型")
    status = serializers.CharField(max_length=32, required=False, help_text="状态")
    labels = serializers.JSONField(binary=False, required=False, help_text="标签")
    unschedulable = serializers.BooleanField(required=False, help_text="可否调度")


class AnnouncementSerilizer(serializers.Serializer):
    content = serializers.CharField(max_length=1000, required=True, help_text=u"通知内容")
    a_tag = serializers.CharField(max_length=256, required=False, help_text=u"A标签文字")
    a_tag_url = serializers.CharField(max_length=1024, required=False, help_text=u"a标签跳转地址")
    type = serializers.CharField(max_length=15, required=False, help_text=u"通知类型")
    active = serializers.BooleanField(required=False, help_text=u"通知是否启用")
    title = serializers.CharField(max_length=64, required=True, help_text=u"通知标题")
    level = serializers.CharField(max_length=32, required=False, help_text=u"通知的等级")


class AccountInitSerilizer(serializers.Serializer):
    user_info = serializers.JSONField(binary=False)
    enterprise_info = serializers.JSONField(binary=False)
