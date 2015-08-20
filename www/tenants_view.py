# -*- coding: utf8 -*-
import logging
import uuid
import hashlib
import datetime
import time
import json

from django.views.decorators.cache import never_cache
from django.template.response import TemplateResponse
from django.http.response import HttpResponse
from django.http import JsonResponse
from www.views import BaseView
from www.models import Tenants
from www.service_http import RegionServiceApi

import logging
logger = logging.getLogger('default')

client = RegionServiceApi()

# 休眠
class TenantsVisitorView(BaseView):
    @never_cache
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST.get("action", "")
            tenants = request.POST.get("tenants", "")
            #logger.debug("action=" + action)
            #logger.debug("tenants=" + tenants)
            if action == "pause":
                if tenants is not None and tenants != "":
                    tenantList = Tenants.objects.filter(service_status=1, pay_type='free')
                    map = {}
                    arr = []
                    for tenant in tenantList:
                        map[tenant.tenant_name] = tenant.tenant_id
                        arr.append(tenant.tenant_name)
                    tses = tenants.split(",")
                    needToPuaseSet = set(arr) - set(tses)
                    # ts = "salogs"
                    logger.debug("pause size=" + str(len(needToPuaseSet)))
                    for ts in needToPuaseSet:
                        try:
                            tenant_id = map[ts]
                            logger.debug(tenant_id)
                            if tenant_id is not None and tenant_id != "":
                                data = client.pause(tenant_id)
                                if data["data"] > 0:
                                    oldTenant = Tenants.objects.get(tenant_id=tenant_id)
                                    oldTenant.service_status = 0
                                    oldTenant.save()
                        except Exception as e0:
                            logger.exception(e0)                                                                    
            elif action == "unpause":
                tenants = request.POST.get("tenants", "")
                if tenants is not None and tenants != "":
                    tses = tenants.split(",")
                    for ts in tses:
                        try:
                            oldTenant = Tenants.objects.get(tenant_name=ts)
                            if oldTenant.service_status == 0:
                                client.unpause(oldTenant.tenant_id)
                                oldTenant.service_status = 1
                                oldTenant.save()
                            else:
                                logger.debug(ts + " not paused")
                        except Exception as e1:
                            logger.exception(e1)
            data["status"] = "success"
        except Exception as e:
            logger.exception(e)
            data["status"] = "failure"
        return JsonResponse(data, status=200)
