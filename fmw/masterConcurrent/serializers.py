from rest_framework import serializers
from fmw.masterConcurrent.models import MasterConcurrent, MasterConcurrentDetail


class MasterConcurrentSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    conc_master_lookup_type_desc = serializers.CharField(source="concurrent_lookup_type_id.lookup_code", read_only=True)
    application__application_name = serializers.CharField(source="application.application_name", read_only=True)
    created_by_name = serializers.ReadOnlyField()
    last_updated_by_name = serializers.ReadOnlyField()

    class Meta:
        model = MasterConcurrent
        # fields = ('id','url', 'concurrent_type','concurrent_name')
        fields = '__all__'
        read_only_fields = ('created_by', 'created_by_name', 'last_updated_by', 'last_updated_by_name')


class MasterConcurrentDetailSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    concurrent_uuid = serializers.UUIDField(source="concurrent_id.concurrent_uuid", read_only=True)

    conc_detail_lookup_type_desc = serializers.CharField(source="concurrent_lookup_param_type_id.description",
                                                         read_only=True)
    conc_detail_lookup_type_meaning = serializers.CharField(source="concurrent_lookup_param_type_id.meaning",
                                                            read_only=True)

    concurrent_lookup_detail_type_code = serializers.CharField(
        source="concurrent_lookup_param_type_id.lookup_code", read_only=True
    )

    concurrent_lookup_detail_value_set_desc = serializers.CharField(
        source="concurrent_lookup_param_value_set_id.description", read_only=True)

    concurrent_lookup_detail_value_set_meaning = serializers.CharField(
        source="concurrent_lookup_param_value_set_id.meaning", read_only=True)

    concurrent_lookup_detail_value_set_code = serializers.CharField(
        source="concurrent_lookup_param_value_set_id.lookup_code", read_only=True
    )

    created_by_name = serializers.ReadOnlyField()

    last_updated_by_name = serializers.ReadOnlyField()

    class Meta:
        model = MasterConcurrentDetail
        # fields = ('id','concurrent_param_uuid','concurrent_id', 'seq','param','type','max_character','enabled_flag','created_by','created_date','last_update_by','last_update_date','concurrent_uuid')
        fields = '__all__'
        read_only_fields = ('created_by', 'created_by_name', 'last_updated_by', 'last_updated_by_name')
