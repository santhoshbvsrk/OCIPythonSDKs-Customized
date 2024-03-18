import oci
import argparse

config = oci.config.from_file()

ns = "<Tenancy Namespace>"
bkt_name = "<OCI Bucket Name>"
files_location = "<Objects Download location>"

object_storage_client = oci.object_storage.ObjectStorageClient(config)

list_objects_response = object_storage_client.list_objects(
    namespace_name=ns,
    bucket_name=bkt_name,
    fields="storageTier,timeCreated")

for i in list_objects_response.data.objects:
    if i.storage_tier == 'Standard':
        object_path = f"{files_location}\{i.name}"
        print(i.name,i.storage_tier)
        get_object_response = object_storage_client.get_object(
            namespace_name=ns,
            bucket_name=bkt_name,
            object_name=i.name)
        with open(object_path, "wb") as f:
                    f.write(get_object_response.data.content)
                    print(f"Downloaded {i.name} to {object_path}")

        update_object_storage_tier_response = object_storage_client.update_object_storage_tier(
               namespace_name=ns,
               bucket_name=bkt_name,
               update_object_storage_tier_details=oci.object_storage.models.UpdateObjectStorageTierDetails(
                      object_name=i.name,
                      storage_tier="Archive"))
        
        print(f"Archived {i.name}")

print(get_object_response.data)
