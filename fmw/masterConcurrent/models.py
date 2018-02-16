from django.db import models
# from django.utils import timezone
from fmw.applications.models import TsApplications
from fmw.lookups.models import TsLookupCodes, TsLookups
import uuid
from fmw.utils.models import TsModel


class MasterConcurrent(TsModel):
    concurrent_uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, blank=False, null=False)
    concurrent_lookup_type_id = models.ForeignKey(TsLookupCodes, on_delete=models.CASCADE, default=1,
                                                  db_column='concurrent_lookup_type_id',
                                                  related_name='lookup_master_conc')
    application = models.ForeignKey(TsApplications, on_delete=models.PROTECT, db_column='application_id',
                                    related_name='concurrent_application')
    url = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, null=True, blank=False)
    concurrent_name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True)

    # concurrent_type = models.IntegerField(null=False,blank=False)

    class Meta:
        db_table = 'ts_concurrent'


class MasterConcurrentDetail(TsModel):
    concurrent_param_uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, blank=False, null=False)
    concurrent_id = models.ForeignKey(MasterConcurrent, on_delete=models.CASCADE, default=1, db_column='concurrent_id',
                                      related_name='master_detail')
    concurrent_lookup_param_type_id = models.ForeignKey(TsLookupCodes, on_delete=models.CASCADE, default=1,
                                                         db_column='concurrent_lookup_param_type_id',
                                                         related_name='lookup_detail_conc')
    seq = models.IntegerField(null=False)
    param = models.CharField(max_length=255, blank=False)
    # type = models.IntegerField(blank=True)
    # type_description = models.CharField(max_length=255, null=True)
    max_character = models.IntegerField(null=True)
    description = models.CharField(max_length=255, null=True)
    enabled_flag = models.CharField(max_length=1, null=True)
    display_flag = models.CharField(max_length=1, null=False)
    required_flag = models.CharField(max_length=1, null=False)
    default_value = models.CharField(max_length=25, null=True)
    concurrent_lookup_param_value_set_id = models.ForeignKey(TsLookupCodes, on_delete=models.CASCADE,null=True,blank=True,
                                                              db_column='concurrent_lookup_detail_value_set_id',
                                                              related_name='lookuptype_det_conc')
    # concurrent_lookup_detail_value_set_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'ts_concurrent_param'
        ordering = ['concurrent_id', 'seq']
