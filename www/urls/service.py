from django.conf.urls import patterns, url
# from www.tests import *
from www.services_view import *
from www.app_services_view import *
from www.back_services_view import *
from www.charging_view import *
from www.views.service import TeamInfo
from django.contrib.auth.decorators import login_required
from www import alipay_view
from django.views.decorators.csrf import csrf_exempt
# from www.views.service import ServicePublishView, ServicePublishExtraView
from www.views.servicepublish import PublishServiceView, PublishServiceRelationView, PublishServiceDetailView
from www.views.license import LicenseViews, LicenseDetailViews, LicenseShow
from www.views.serviceshare import ShareServiceImageView, ShareServiceStep1View, \
    ShareServiceStep2View, ShareServiceStep3View


urlpatterns = patterns(
    '',
    url(r'^/?$', login_required(TenantServiceAll.as_view())),

    url(r'^/app-create/$', login_required(AppCreateView.as_view())),

    url(r'^/(?P<serviceAlias>[\w\-]+)/app-waiting/$', login_required(AppWaitingCodeView.as_view())),

    url(r'^/(?P<serviceAlias>[\w\-]+)/app-language/$', login_required(AppLanguageCodeView.as_view())),

    url(r'^/(?P<serviceAlias>[\w\-]+)/app-dependency/$', login_required(AppDependencyCodeView.as_view())),
    # url(r'^/(?P<serviceAlias>[\w\-]+)/publish/$', ServicePublishView.as_view()),
    # url(r'^/(?P<serviceAlias>[\w\-]+)/publish/extra/?$', ServicePublishExtraView.as_view()),
    url(r'^/(?P<serviceAlias>[\w\-]+)/setup/extra/?$', ServiceDeployExtraView.as_view()),

    url(r'^/service/$', login_required(ServiceMarket.as_view())),

    url(r'^/service-deploy/$', login_required(ServiceMarketDeploy.as_view())),

    url(r'^/team/$', TeamInfo.as_view()),

    url(r'^/(?P<serviceAlias>[\w\-]+)/detail/?$', login_required(TenantService.as_view())),

    url(r'^/(?P<serviceAlias>[\w\-]+)/latest-log/$', login_required(ServiceLatestLog.as_view())),
    url(r'^/(?P<serviceAlias>[\w\-]+)/history-log/$', login_required(ServiceHistoryLog.as_view())),
    url(r'^/(?P<serviceAlias>[\w\-]+)/docker/$', login_required(ServiceDockerContainer.as_view())),

    url(r'^/recharge/$', login_required(Recharging.as_view())),
    url(r'^/consume/$', login_required(Account.as_view())),
    url(r'^/bill/$', login_required(AccountBill.as_view())),
    url(r'^/paymodel/$', login_required(PayModelView.as_view())),

    url(r'^/recharge/alipay$', csrf_exempt(login_required(alipay_view.submit))),
    url(r'^/recharge/alipay-return$', alipay_view.return_url),
    url(r'^/recharge/alipay-notify$', alipay_view.notify_url),

    # new publish service
    url(r'^/(?P<serviceAlias>[\w\-]+)/publish/$', PublishServiceDetailView.as_view()),
    url(r'^/(?P<serviceAlias>[\w\-]+)/publish/relation/?$', PublishServiceRelationView.as_view()),
    url(r'^/(?P<serviceAlias>[\w\-]+)/publish/extra/?$', PublishServiceView.as_view()),

    # new share service
    url(r'^/(?P<serviceAlias>[\w\-]+)/share/step1$', ShareServiceStep1View.as_view()),
    url(r'^/(?P<serviceAlias>[\w\-]+)/share/step2$', ShareServiceStep2View.as_view()),
    url(r'^/(?P<serviceAlias>[\w\-]+)/share/step3$', ShareServiceStep3View.as_view()),
    url(r'^/(?P<serviceAlias>[\w\-]+)/share/images$', ShareServiceImageView.as_view()),

    # license service
    url(r'^/license-list$', login_required(LicenseViews.as_view())),
    url(r'^/license-detail$', login_required(LicenseDetailViews.as_view())),
    url(r'^/license-show$', LicenseShow.as_view()),
)
