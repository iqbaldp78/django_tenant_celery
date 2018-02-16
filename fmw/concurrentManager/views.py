from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django_celery_results.models import TaskResult
from fmw.concurrentManager.models import ConcurrentList
from fmw.concurrentManager.serializers import ConcurrentSerializer \
    # ,ListSerializer
from fmw.concurrentManager.tasks import concurrent
from celery.result import AsyncResult
from django_filters import rest_framework as filters
from fmw.utils import filter
from django.db import connection
from fmw.masterConcurrent.models import MasterConcurrent
from fmw.lookups.models import TsLookupCodes



class concurrentListFilter(filter.TsFilterSet):
    url = filters.CharFilter(lookup_expr='icontains',name='concurrent_id__url')
    concurrent_name = filters.CharFilter(lookup_expr='icontains', name='concurrent_id__concurrent_name')
    run_type_desc = filters.CharFilter(lookup_expr='icontains', name='run_type__description')
    run_type_meaning = filters.CharFilter(lookup_expr='icontains', name='run_type__meaning')
    run_type_lookup_code = filters.CharFilter(lookup_expr='icontains', name='run_type__meaning')
    class Meta(filter.TsFilterSet.Meta):
        model = ConcurrentList
        fields = '__all__'


class concurrentListViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    queryset = ConcurrentList.objects.all()
    serializer_class = ConcurrentSerializer
    lookup_field = 'concurrent_req_uuid'
    filter_class = concurrentListFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = ConcurrentList.objects.raw('''
                            SELECT 
                            C.id,
                            C.run_type,
                            case when
                                    D.status is null then 'PENDING'
                                when 
                                    D.status = 'SUCCESS' then 'RUNNING'
                                else D.status
                            end as phase, 
                            c.status,
                            c.start_date,
                            c.end_date,
                            c.param_value,
                            c.interval_run,
                            c.task_id,
                            c.created_by,
                            c.creation_date,
                            c.last_update_date,
                            c.last_updated_by,
                            d.date_done as actual_end_date,
                            c.login_id 
                            FROM "ts_concurrent_request" C
                            LEFT JOIN "django_celery_results_taskresult" d
                            ON (c.task_id = d.task_id) 
                            ''')
        a = list(data)
        # print(a)
        # update data phase di concurrent List berdasarkan serializer conc
        for datax in a :
            # print(datax.phase)
            if datax.phase != "PENDING":
                data = ConcurrentList.objects.get(id=datax.id)
                data.phase=datax.phase
                datax.save()

        serializer = self.get_serializer(data=request.data)
        # print(serializer.data)
        # print(serializer.data['id'])

        # data = ConcurrentList.objects.get(id=serializer.data['id'])



        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        schema_name = connection.schema_name
        # print('schemasnya %s'%schema_name)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        req_id = serializer.data['id']

        conc_id = serializer.data['concurrent_id']
        # print('conc_id %s' % conc_id)
        data_master_conc = MasterConcurrent.objects.get(id=conc_id)
        # print('conc_id %s' % data_master_conc.url)
        url = data_master_conc.url

        # url = serializer.data['url']
        param_value = serializer.data['param_value']
        conc_type_id = serializer.data['run_type']
        # print(serializer.data)
        conc_type = TsLookupCodes.objects.get(id=conc_type_id)
        # print("serializer NYA %s" % (serializer.data))
        if conc_type.lookup_code == 'ADHOC':
            concurrent.delay(url, param_value, req_id,schema_name)
            tasks = TaskResult.objects.all()
            # print('ini task %s' % tasks)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.id, last_updated_by=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save(last_updated_by=self.request.user.id)


# update status flag di concurrent
def update_stat_flag(req_id, new_stat=None,new_phase=None):
    print('Masuk update flag')
    try:
        data = ConcurrentList.objects.get(id=req_id)
        data.status = new_stat
        data.phase = new_phase
        data.save()
        return data
    except ConcurrentList.DoesNotExist:
        data = "data ga ada"
        return data
