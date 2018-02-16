# from rest_framework.utils import json
import json

import requests
from celery import current_task
from django.utils import timezone
from fmw.concurrentManager.models import ConcurrentList
from harpa.celery import app
from django.db import connection
from datetime import timedelta
from tenant_schemas.utils import schema_context, get_public_schema_name
from fmw.clients.models import TsClients
from celery.result import AsyncResult
import datetime
# import pytz
from fmw.masterConcurrent.models import MasterConcurrent
# from fmw.lookups.models import TsLookupCodes



@app.task()
def concurrent(url, param_value, req_id, schema):
    # time.sleep(10)
    with schema_context(schema_name=schema):
        skema = connection.schema_name
        print(connection.schema_name)
        result = current_task.request.id
        tgl = datetime.datetime.now()
        print('sysdate %s' % tgl)
        get_data = ConcurrentList.objects.get(id=req_id)
        get_data.task_id = result
        get_data.actual_start_date = tgl
        get_data.phase = 'S'
        get_data.save()

        json_acceptable_string = param_value.replace("'", "\"")
        x = json.loads(json_acceptable_string)
        print("http://" + schema + ".harpa.com:8000/login/")
        headers1 = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r1 = requests.post("http://" + schema + ".harpa.com:8000/login/",
                           {"user_name": "sysadmin@" + schema + ".harpa.com", "password": "welcome"})
        # print("return API %s" % r1 )
        response_data = r1.json()

        print(response_data)

        # # print("=================================================")
        a = 'JWT ' + response_data['token']
        # # print("=================================================")
        # # print("=================================================")
        # # print("=================================================")
        print('JWT %s' % a)
        # # print("=================================================")
        # # print("=================================================")
        # # print("=================================================")
        headers = {"Content-type": 'application/json', 'Accept': 'application/json', 'Authorization': a}
        # # print("=================================================")
        # # print("=================================================")
        # # print("=================================================")
        #
        # # print('ini headers %s'%headers)
        # # print('data=json.dumps(x) %s'% json.dumps(x))
        r = requests.post(url, data=json.dumps(x), headers=headers)
        # # print(r.text)
        response_data2 = r.json()
        print('response_data2 = %s' % r)
        #
        # # print(result)
        # print('schema name %s' % (connection.schema_name))
        res = AsyncResult(result)
        res.ready()
        # print ('status nya %s'%res.ready())
        # print ('status nya %s'% AsyncResult(current_task.request.id).state)
        # print ('sysdate %s' % tgl)
    return 'berhasil'


@app.task
def concurrent_schedule():
    print("mulai")
    get_schema = TsClients.objects.exclude(schema_name='public')
    # print(get_schema)
    a = list(get_schema)
    for datax in a:
        skema = datax.schema_name
        print('skema nya %s' % skema)
        with schema_context(schema_name=skema):
            print('connection.schema_name %s' % connection.schema_name)
            # ga tau kenapa ga bisa pake objects.get()
            # lookup_code_id_adhoc = TsLookupCodes.objects.filter(lookup_code = "ADHOC")
            # for a in lookup_code_id_adhoc:
            #     # print(a.id)
            #     b = a.id
            #
            # lookup_code = b
            # ga bisa diselect lookup_nya
            get_list_concurrent = ConcurrentList.objects.exclude(run_type=421).filter(
                phase='PENDING').order_by(
                'id')

            # get list all scheduler type
            for get_object in get_list_concurrent:
                tgl_awal = get_object.start_date
                print('request id %s and start_date %s sysdate %s' % ((get_object.id, tgl_awal, timezone.now())))
                print('TGL awal start_date %s' % tgl_awal)
                print('sysdatenya %s' % (timezone.now()))
                print('===============================')
                print('===============================')
                # print('jalan om sesuai start_date enddatenya')
                # url = get_object.url
                conc_id = get_object.concurrent_id.id
                print('concurrent_id %s' % conc_id)
                data_master_conc = MasterConcurrent.objects.get(id=conc_id)
                url = data_master_conc.url
                print('url %s' % url)
                param_value = get_object.param_value
                concurrent_id = get_object.concurrent_id
                req_id = get_object.id

                print(get_object.run_type.lookup_code)
                if datetime.datetime.now() >= tgl_awal and get_object.phase == 'PENDING' and get_object.run_type.lookup_code == 'ONCE':  # ONCE
                    print("jalan Once")
                    concurrent.delay(url, param_value, req_id, skema)
                    get_object.phase = 'S'
                    get_object.save()
                    print('Update phase S utk req id %s' % get_object.id)



                elif timezone.now() >= tgl_awal and get_object.phase == 'PENDING' and get_object.run_type.lookup_code == 'PERIODICALLY':  # PERIODICALLY
                    print("jalan Periodically")

                    if get_object.interval_run_type == 'MONTHLY':
                        print("MONTHLY Periodically")

                        concurrent.delay(url, param_value, req_id, skema)

                        # update flag phase
                        get_object.phase = 'S'
                        get_object.save()
                        print('Update phase S utk req id %s' % get_object.id)
                        nexttime = (get_object.start_date + timedelta(months=get_object.interval_run))
                        print('Next Time min %s' % nexttime)
                        if nexttime <= get_object.end_date:
                            print('insert new record')
                            # insert next schedule
                            insert_master_conc = ConcurrentList(run_type=get_object.run_type,
                                                                # url=url,
                                                                # concurrent_name=get_object.concurrent_name,
                                                                phase='PENDING',
                                                                status=None,
                                                                parent_req_id=get_object.parent_req_id,
                                                                start_date=nexttime,
                                                                end_date=get_object.end_date,
                                                                param_value=param_value,
                                                                interval_run_type = get_object.interval_run_type,
                                                                interval_run=get_object.interval_run,
                                                                task_id=None,
                                                                concurrent_id=concurrent_id,
                                                                created_by=get_object.created_by,
                                                                creation_date=get_object.creation_date,
                                                                last_updated_by=get_object.last_updated_by,
                                                                last_update_date=get_object.last_update_date,
                                                                login_id=get_object.login_id
                                                                )
                            insert_master_conc.save()

                    elif get_object.interval_run_type == 'WEEKLY':
                        print("WEEKLY Periodically")

                        concurrent.delay(url, param_value, req_id, skema)

                        # update flag phase
                        get_object.phase = 'S'
                        get_object.save()
                        print('Update phase S utk req id %s' % get_object.id)
                        nexttime = (get_object.start_date + timedelta(weeks=get_object.interval_run))
                        print('Next Time min %s' % nexttime)
                        if nexttime <= get_object.end_date:
                            print('insert new record')
                            # insert next schedule
                            insert_master_conc = ConcurrentList(
                                # url=url,
                                # concurrent_name=get_object.concurrent_name,
                                run_type=get_object.run_type,
                                phase='PENDING',
                                status=None,
                                parent_req_id=get_object.parent_req_id,
                                start_date=nexttime,
                                end_date=get_object.end_date,
                                param_value=param_value,
                                interval_run_type=get_object.interval_run_type,
                                interval_run=get_object.interval_run,
                                task_id=None,
                                concurrent_id=concurrent_id,
                                created_by=get_object.created_by,
                                creation_date=get_object.creation_date,
                                last_updated_by=get_object.last_updated_by,
                                last_update_date=get_object.last_update_date,
                                login_id=get_object.login_id
                            )
                            insert_master_conc.save()

                    elif get_object.interval_run_type == 'DAILY':
                        print("DAILY Periodically")

                        concurrent.delay(url, param_value, req_id, skema)

                        # update flag phase
                        get_object.phase = 'S'
                        get_object.save()
                        print('Update phase S utk req id %s' % get_object.id)
                        nexttime = (get_object.start_date + timedelta(days=get_object.interval_run))
                        print('Next Time min %s' % nexttime)
                        if nexttime <= get_object.end_date:
                            print('insert new record')
                            # insert next schedule
                            insert_master_conc = ConcurrentList(
                                # url=url,
                                # concurrent_name=get_object.concurrent_name,
                                run_type=get_object.run_type,
                                phase='PENDING',
                                status=None,
                                parent_req_id=get_object.parent_req_id,
                                start_date=nexttime,
                                end_date=get_object.end_date,
                                param_value=param_value,
                                interval_run_type=get_object.interval_run_type,
                                interval_run=get_object.interval_run,
                                task_id=None,
                                concurrent_id=concurrent_id,
                                created_by=get_object.created_by,
                                creation_date=get_object.creation_date,
                                last_updated_by=get_object.last_updated_by,
                                last_update_date=get_object.last_update_date,
                                login_id=get_object.login_id
                            )
                            insert_master_conc.save()

                    elif get_object.interval_run_type == 'HOURS':
                        print("HOURS Periodically")

                        concurrent.delay(url, param_value, req_id, skema)

                        # update flag phase
                        get_object.phase = 'S'
                        get_object.save()
                        print('Update phase S utk req id %s' % get_object.id)
                        nexttime = (get_object.start_date + timedelta(hours=get_object.interval_run))
                        print('Next Time min %s' % nexttime)
                        if nexttime <= get_object.end_date:
                            print('insert new record')
                            # insert next schedule
                            insert_master_conc = ConcurrentList(
                                # url=url,
                                #                                 concurrent_name=get_object.concurrent_name,
                                run_type=get_object.run_type,
                                phase='PENDING',
                                status=None,
                                parent_req_id=get_object.parent_req_id,
                                start_date=nexttime,
                                end_date=get_object.end_date,
                                param_value=param_value,
                                interval_run_type=get_object.interval_run_type,
                                interval_run=get_object.interval_run,
                                task_id=None,
                                concurrent_id=concurrent_id,
                                created_by=get_object.created_by,
                                creation_date=get_object.creation_date,
                                last_updated_by=get_object.last_updated_by,
                                last_update_date=get_object.last_update_date,
                                login_id=get_object.login_id
                            )
                            insert_master_conc.save()

                    elif get_object.interval_run_type == 'MINUTES':
                        print("MINUTES Periodically")

                        concurrent.delay(url, param_value, req_id, skema)

                        # update flag phase
                        get_object.phase = 'S'
                        get_object.save()
                        print('Update phase S utk req id %s' % get_object.id)
                        nexttime = (get_object.start_date + timedelta(minutes=get_object.interval_run))
                        print('Next Time min %s' % nexttime)
                        if nexttime <= get_object.end_date:
                            print('insert new record')
                            # insert next schedule
                            insert_master_conc = ConcurrentList(
                                # url=url,
                                #                                 concurrent_name=get_object.concurrent_name,
                                run_type=get_object.run_type,
                                phase='PENDING',
                                status=None,
                                parent_req_id=get_object.parent_req_id,
                                start_date=nexttime,
                                end_date=get_object.end_date,
                                param_value=param_value,
                                interval_run_type=get_object.interval_run_type,
                                interval_run=get_object.interval_run,
                                task_id=None,
                                concurrent_id=concurrent_id,
                                created_by=get_object.created_by,
                                creation_date=get_object.creation_date,
                                last_updated_by=get_object.last_updated_by,
                                last_update_date=get_object.last_update_date,
                                login_id=get_object.login_id
                            )
                            insert_master_conc.save()

                else:
                    print('sabar om')
        print('==========================================================')
        print('==========================================================')
        print('==========================================================')
        print('==========================================================')
        print('==========================================================')
        print('==========================================================')
        print('==========================================================')
    return 'berhasil'
