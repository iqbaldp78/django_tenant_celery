from django.db import models
from django.utils import timezone
import uuid
from fmw.masterConcurrent.models import MasterConcurrent
from fmw.utils.models import TsModel
from fmw.lookups.models import TsLookupCodes, TsLookups
from django.core.exceptions import ValidationError


class ConcurrentList(TsModel):
    concurrent_req_uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, blank=False, null=False)
    run_type = models.ForeignKey(TsLookupCodes, on_delete=models.CASCADE, null=True, blank=True,
                                 db_column='run_type',
                                 related_name='lookup_run_type')
    phase = models.CharField(max_length=255, default='PENDING', blank=False, null=False)
    status = models.CharField(max_length=255, blank=True, null=True)
    parent_req_id = models.CharField(max_length=255, blank=True, null=True)
    interval_run_type = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    param_value = models.CharField(db_index=True, max_length=1000, blank=False, null=False)
    param_value_meaning = models.CharField(max_length=255, blank=True, null=True)
    interval_run = models.IntegerField(blank=True, null=True)
    task_id = models.CharField(db_index=True, max_length=255, blank=True, null=True)
    concurrent_id = models.ForeignKey(MasterConcurrent, blank=False, null=False, on_delete=models.DO_NOTHING,
                                      db_column='concurrent_id',
                                      related_name='ts_concurrent_request')
    actual_start_date = models.DateTimeField(blank=True, null=True)
    actual_end_date = models.DateTimeField(blank=True, null=True)

    # date_submit = models.DateTimeField(blank=True, null=True,default=timezone.now)

    class Meta:
        db_table = 'ts_concurrent_request'
        ordering = ['-id']

    # def clean(self):
    #     if self.end_date < self.start_date:
    #         raise ValidationError("End date must be greather than start date.")
