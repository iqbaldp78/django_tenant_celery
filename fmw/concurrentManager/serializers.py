from rest_framework import serializers

from fmw.concurrentManager.models import ConcurrentList


class ConcurrentSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="concurrent_id.url", read_only=True)
    concurrent_name = serializers.CharField(source="concurrent_id.concurrent_name", read_only=True)

    run_type_desc = serializers.CharField(source="run_type.description", read_only=True)
    run_type_meaning = serializers.CharField(source="run_type.meaning", read_only=True)
    run_type_lookupcode = serializers.CharField(source="run_type.lookup_code", read_only=True)

    concurrent_lookup_type_meaning = serializers.CharField(source="concurrent_id.concurrent_lookup_type_id.meaning",
                                                           read_only=True)
    concurrent_lookup_type_desc = serializers.CharField(source="concurrent_id.concurrent_lookup_type_id.description",
                                                           read_only=True)
    concurrent_lookup_type_lookupcode = serializers.CharField(source="concurrent_id.concurrent_lookup_type_id.lookup_code",
                                                           read_only=True)

    created_by_name = serializers.ReadOnlyField()
    last_updated_by_name = serializers.ReadOnlyField()

    class Meta:
        model = ConcurrentList
        fields = '__all__'
        read_only_fields = ('created_by', 'created_by_name', 'last_updated_by', 'last_updated_by_name')

    # def validate_end_date(self, value):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     if 1 == 1:
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return value

    # def validate_phase(self, value):
    #     a = value['concurrent_name']
    #     print(a)
    #     b = value['concurrent_name']
    #     print(b)
    #     if 1 == 1:
    #         raise serializers.ValidationError("Ficha no publicada")
    #     return value

    # def validate_interval_run(self, value):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     a = value.get('start_date', self.instance.start_date)
    #     print(a)
    #     if 1 == 1:
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return value


    # def validate(self, data):
    #     """
    #     Check that the enddate is greather than startdate.
    #     """
    #     if (data['end_date'] and data['start_date']) is not None :
    #         print("Masuk")
    #         if data['end_date'] < data['start_date']:
    #             raise serializers.ValidationError("end_date must be greathe than start_date")
    #         return data
    #     else :
    #         print("ga masuk")