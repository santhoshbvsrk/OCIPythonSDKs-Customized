#working to attach block volume to VM
import InputData_VM
import time
import oci
from oci.config import from_file
from oci.core.models import CreateVnicDetails, InstanceSourceViaBootVolumeDetails, LaunchInstanceDetails, LaunchInstanceShapeConfigDetails, AttachVolumeDetails
from oci.core import BlockstorageClient
from oci.core import ComputeClient

# Read configuration from a file. You can generate this file using "oci setup config"
config = from_file("~/.oci/config")

# Initialize Compute Client
compute_client = ComputeClient(config)

# Create VNIC Details
vnic_details = CreateVnicDetails(subnet_id=InputData_VM.subnet_id, assign_public_ip=True)

# Boot Volume Details
boot_volume_details = InstanceSourceViaBootVolumeDetails(boot_volume_id=InputData_VM.boot_volume_id)

# Create Instance Details
instance_details = LaunchInstanceDetails(
    availability_domain=InputData_VM.availability_domain,
    compartment_id=InputData_VM.compartment_id,
    display_name=InputData_VM.display_name,
    image_id=InputData_VM.image_id,
    shape=InputData_VM.shape,
    shape_config=LaunchInstanceShapeConfigDetails(
            ocpus=InputData_VM.ocpus,
            memory_in_gbs=InputData_VM.memory_in_gbs),
    create_vnic_details=vnic_details,
    source_details=boot_volume_details
)

# Create the instance
response = compute_client.launch_instance(instance_details)
get_instance_response = compute_client.get_instance(instance_id=response.data.id)
getinst_data = get_instance_response.data

while getinst_data.lifecycle_state != "RUNNING":
    time.sleep(10)
    get_instance_response = compute_client.get_instance(instance_id=response.data.id)
    getinst_data = get_instance_response.data

print('VM is created from Boot Volume successfully. Will attach Block Volume now')

# attach block volume to VM
def attach_block_volume(compute_client, blockstorage_client, instance_id, volume_id,type):
    attach_volume_details = AttachVolumeDetails(
        instance_id=instance_id,
        volume_id=volume_id,
        type=type
    )
    response = compute_client.attach_volume(attach_volume_details)
    print("Attached Block Volume to OCI VM")

# initialize blockstorage client
blockstorage_client = BlockstorageClient(config)

# pass instance ID and volume ID to the function
instance_id=response.data.id
volume_id = InputData_VM.volume_id
type = InputData_VM.type
attach_block_volume(compute_client, blockstorage_client, instance_id, volume_id,type)
