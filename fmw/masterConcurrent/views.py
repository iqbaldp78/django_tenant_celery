from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters
from fmw.masterConcurrent.models import MasterConcurrent, MasterConcurrentDetail
from fmw.masterConcurrent.serializers import MasterConcurrentDetailSerializer, MasterConcurrentSerializer
from fmw.utils import filter


class MasterConcFilter(filter.TsFilterSet):
    conc_master_lookup_type_desc = filters.CharFilter(name='concurrent_lookup_type_id__lookup_code')
    application__application_name = filters.CharFilter(name='application__application_name')
    class Meta(filter.TsFilterSet.Meta):
        model = MasterConcurrent
        fields = '__all__'


class ConcurrentCreateViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              viewsets.GenericViewSet):
    queryset = MasterConcurrent.objects.all()
    serializer_class = MasterConcurrentSerializer
    filter_class = MasterConcFilter
    lookup_field = 'concurrent_uuid'

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.id, last_updated_by=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save(last_updated_by=self.request.user.id)


class MasterDetailConcFilter(filter.TsFilterSet):
    concurrent_uuid = filters.UUIDFilter(name="concurrent_id__concurrent_uuid")

    conc_detail_lookup_type_desc = filters.CharFilter(lookup_expr='icontains',
                                                      name='concurrent_lookup_param_type_id__description')

    conc_detail_lookup_type_meaning = filters.CharFilter(lookup_expr='icontains',
                                                         name='concurrent_lookup_param_type_id__meaning')

    concurrent_lookup_detail_value_set_desc = filters.CharFilter(lookup_expr='icontains',
                                                                 name='concurrent_lookup_param_value_set_id__description')

    concurrent_lookup_detail_value_set_meaning = filters.CharFilter(lookup_expr='icontains',
                                                                    name='concurrent_lookup_param_value_set_id__meaning')

    concurrent_lookup_detail_type_code = filters.CharFilter(lookup_expr='icontains',
                                                            name='concurrent_lookup_param_type_id__lookup_code')

    concurrent_lookup_detail_value_set_code = filters.CharFilter(lookup_expr='icontains',
                                                                 name='concurrent_lookup_param_value_set_id__lookup_code')

    class Meta(filter.TsFilterSet.Meta):
        model = MasterConcurrentDetail
        fields = '__all__'
        order_by = True


class ConcurrentDetailCreateViewSet(mixins.ListModelMixin,
                                    mixins.CreateModelMixin,
                                    mixins.DestroyModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    viewsets.GenericViewSet):
    lookup_field = 'concurrent_param_uuid'
    queryset = MasterConcurrentDetail.objects.all()
    filter_class = MasterDetailConcFilter
    serializer_class = MasterConcurrentDetailSerializer

    def list(self, request, *args, **kwargs):
        showAll = request.query_params.get('showAll')
        if showAll == False or showAll == None:
            test = super().list(request, *args, **kwargs)
            return test
        else:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.id, last_updated_by=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save(last_updated_by=self.request.user.id)
