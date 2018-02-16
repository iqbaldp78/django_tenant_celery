"""harpa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

schema_view = get_swagger_view(title='HARPA API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', schema_view),

    url(r'^users/', include('fmw.users.urls', namespace='users')),
    url(r'^companyGroups/', include('fmw.clients.urls', namespace='clients')),
    url(r'^menus/', include('fmw.menus.urls', namespace='menus')),
    url(r'^currencies/', include('fmw.currencies.urls')),
    url(r'^pages/', include('fmw.pages.urls')),
    url(r'^applications/', include('fmw.applications.urls')),
    url(r'^lookups/', include('fmw.lookups.urls')),
    url(r'^flexfield/', include('fmw.flexfield.urls')),
    url(r'^functions/', include('fmw.functions.urls')),
    url(r'^roles/', include('fmw.roles.urls', namespace='roles')),
    url(r'^request_groups/', include('fmw.request_groups.urls', namespace='request_groups')),
    url(r'^profiles/', include('fmw.profiles.urls', namespace='profiles')),
    url(r'^user_profiles/', include('fmw.user_profiles.urls', namespace='user_profiles')),
    url(r'^currencyRates/', include('fmw.currencyRates.urls')),
    url(r'^securityProfiles/', include('fmw.security_profiles.urls')),

    url(r'^messages/',include('fmw.fmwMessages.urls')),

    url(r'^attachments/', include('fmw.attachments.urls')),

    # concurrent
    url(r'^concurrent/', include('fmw.concurrentManager.urls')),
    url(r'^concurrent/', include('fmw.masterConcurrent.urls')),

    #HR
    url(r'^grades/', include('hr.grades.urls')),
    url(r'^gradeRates/', include('hr.gradeRates.urls')),
    url(r'^jobs/', include('hr.jobs.urls')),
    url(r'^locations/', include('hr.locations.urls')),
    url(r'^organizations/', include('hr.organizations.urls')),
    url(r'^organizationHierarchies/', include('hr.organizationHierarchies.urls')),
    url(r'^positions/', include('hr.positions.urls')),
    url(r'^positionHierarchies/', include('hr.positionHierarchies.urls')),
    url(r'^calendarEvents/', include('hr.calendarEvents.urls')),
    url(r'^performanceAppraisals/', include('hr.performanceAppraisals.urls')),
    #Payroll

    url(r'^variables/', include('payroll.variables.urls')),
    url(r'^payrollGroups/', include('payroll.payrollGroups.urls')),
    url(r'^paymentMethods/', include('payroll.paymentMethods.urls')),
    url(r'^componentClassifications/', include('payroll.componentClassifications.urls')),
    url(r'^components/', include('payroll.components.urls')),
    url(r'^balances/', include('payroll.balances.urls')),
    url(r'^userTables/', include('payroll.userTables.urls')),
    url(r'^componentSets/', include('payroll.componentSets.urls')),
    url(r'^salaryBases/', include('payroll.salaryBases.urls')),
    url(r'^componentLinks/', include('payroll.componentLinks.urls')),
    url(r'^employmentProcessSets/', include('payroll.employmentProcessSets.urls')),
    url(r'^payrollFunctions/', include('payroll.payrollFunctions.urls')),


    #HrTransactions
    url(r'^employees/', include('hrTransaction.employees.urls', namespace='employees')),
    url(r'^employeePayrolls/', include('hrTransaction.employeePayrolls.urls')),
    #PayrollTransactions
    url(r'^componentEntries/', include('payrollTransaction.componentEntries.urls')),
    url(r'^componentEntryBatches/', include('payrollTransaction.componentEntryBatches.urls')),
    url(r'^payrollRuns/', include('payrollTransaction.payrollRuns.urls')),
#    url(r'^prePayment/', include('payrollTransaction.prePayment.urls')),
    url(r'^balanceAccumulator/', include('payrollTransaction.balanceAccumulator.urls')),

    # url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^login-auth/', include('fmw.login.urls', namespace='login-auth')),
    url(r'^login/', include('fmw.users_multi_tenant.urls', namespace='login')),
]
