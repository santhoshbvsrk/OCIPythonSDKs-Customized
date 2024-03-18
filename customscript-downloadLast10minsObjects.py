import oci
import argparse
from datetime import datetime, timezone, timedelta

config = oci.config.from_file()

ns = "<Tenancy Namespace>"
bkt_name = "<Bucket Name>"
files_location = "<Download Location for files"

object_storage_client = oci.object_storage.ObjectStorageClient(config)

list_objects_response = object_storage_client.list_objects(
    namespace_name=ns,
    bucket_name=bkt_name,
    fields="storageTier,timeCreated")

for i in list_objects_response.data.objects:
    if i.storage_tier == 'Standard':
        object_path = f"{files_location}\{i.name}"
        print(i.name,i.storage_tier)
        curr_time = datetime.now(timezone.utc)
        if int(((curr_time - i.time_created).total_seconds()/60)) <= 10:   #here I am setting the time gap to 10minutes, so that it will pick files uploaded in the last 10 minutes only in UTC timezone
            print('***Start of If Loop*****')
            print('File Name:',i.name)
            print('Storage Tier:',i.storage_tier)
            print('Time Created:',i.time_created)
            print('Current Time:',curr_time)
            difference = curr_time - i.time_created
            minutes_diff = int((difference.total_seconds()/60))
            print(f"Difference in minutes:{minutes_diff} minutes")
            print('****End of If Loop*******')
            get_object_response = object_storage_client.get_object(
                namespace_name=ns,
                bucket_name=bkt_name,
                object_name=i.name)
            with open(object_path, "wb") as f:
                        f.write(get_object_response.data.content)
                        print(f"Downloaded {i.name} to {object_path}")

print(get_object_response.data)
