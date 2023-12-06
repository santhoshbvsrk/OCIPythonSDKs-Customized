# Working to create BootVolume from BootVolumeReplicas
import InputData_VM
import time
import oci
from oci.config import from_file
from oci.core.models import CreateVnicDetails, InstanceSourceViaBootVolumeDetails, LaunchInstanceDetails, LaunchInstanceShapeConfigDetails, AttachVolumeDetails, CreateBootVolumeDetails , BootVolumeSourceFromBootVolumeDetails, CreateVolumeDetails, BlockVolumeReplicaDetails, BootVolumeReplicaDetails
from oci.core import BlockstorageClient
from oci.core import ComputeClient

#default profile
config = oci.config.from_file()

# Initialize service client with default config file
core_client = BlockstorageClient(config)

# Send the request to service, some parameters are not required, see API
create_boot_volume_response = core_client.create_boot_volume(
    create_boot_volume_details=CreateBootVolumeDetails(
        compartment_id=InputData_VM.compartment_id,
        source_details=BootVolumeSourceFromBootVolumeDetails(
            id = InputData_VM.boot_vol_replica_id,
            type= InputData_VM.create_boot_type),
        availability_domain=InputData_VM.availability_domain,
        display_name=InputData_VM.boot_vol_name,
        size_in_gbs=InputData_VM.boot_vol_size_in_gbs,
        vpus_per_gb=InputData_VM.boot_vol_vpus_per_gb,
        is_auto_tune_enabled=InputData_VM.is_auto_tune_enabled,
        boot_volume_replicas=[
            oci.core.models.BootVolumeReplicaDetails(
                availability_domain=InputData_VM.bootvolreplica_availability_domain,
                display_name=InputData_VM.bootvolreplica_name)]
        )
)

# Get the data from response
create_bootvol_response=create_boot_volume_response.data

#checkig boot volume creation status from bootvolume replica
get_boot_volume_response = core_client.get_boot_volume(boot_volume_id=create_bootvol_response.id)
get_boot_response = get_boot_volume_response.data

while get_boot_response.lifecycle_state != "AVAILABLE":
    time.sleep(10)
    get_boot_volume_response = core_client.get_boot_volume(boot_volume_id=create_bootvol_response.id)
    get_boot_response = get_boot_volume_response.data
    
print('Boot Volume is created from BootVolumeReplica with OCID:',get_boot_response.id,'with status:',get_boot_response.lifecycle_state)

#Create VM from activated Boot Volume
# Initialize Compute Client
compute_client = ComputeClient(config)

# Create VNIC Details
vnic_details = CreateVnicDetails(subnet_id=InputData_VM.subnet_id, assign_public_ip=InputData_VM.vm_assign_public_ip,private_ip=InputData_VM.vm_private_ip)

# Boot Volume Details
boot_volume_details = InstanceSourceViaBootVolumeDetails(boot_volume_id=create_bootvol_response.id)

# Create Instance Details
instance_details = LaunchInstanceDetails(
    availability_domain=InputData_VM.availability_domain,
    compartment_id=InputData_VM.compartment_id,
    display_name=InputData_VM.vm_display_name,
    image_id=get_boot_response.image_id,
    shape=InputData_VM.vm_shape,
    shape_config=LaunchInstanceShapeConfigDetails(
            ocpus=InputData_VM.vm_ocpus,
            memory_in_gbs=InputData_VM.vm_memory_in_gbs),
    create_vnic_details=vnic_details,
    source_details=boot_volume_details
)

# Create the instance
response = compute_client.launch_instance(instance_details)

#checking for VM creation status
get_instance_response = compute_client.get_instance(instance_id=response.data.id)
getinst_data = get_instance_response.data

while getinst_data.lifecycle_state != "RUNNING":
    time.sleep(10)
    get_instance_response = compute_client.get_instance(instance_id=response.data.id)
    getinst_data = get_instance_response.data

print('VM is created successfully from Boot Volume with OCID:',getinst_data.id,'with status:',getinst_data.lifecycle_state)

# Working to create BlockVolume from BlockVolumeReplicas
# Initialize service client with default config file
core_client = BlockstorageClient(config)

blkvolocid = InputData_VM.block_vol_replica_ocid

for i in range(len(blkvolocid['block_vol_replica_id'])):
    create_volume_response = core_client.create_volume(
        create_volume_details=CreateVolumeDetails(
        compartment_id=InputData_VM.compartment_id,
        availability_domain=InputData_VM.availability_domain,
        display_name=blkvolocid['block_vol_name'][i],
        vpus_per_gb=blkvolocid['blockvol_vpus_per_gb'][i],
        size_in_gbs=blkvolocid['blockvol_size_in_gbs'][i],
        source_details=oci.core.models.VolumeSourceFromBlockVolumeReplicaDetails(
            type="blockVolumeReplica",
            id=blkvolocid['block_vol_replica_id'][i]),
        is_auto_tune_enabled=InputData_VM.is_auto_tune_enabled,
        block_volume_replicas=[
            BlockVolumeReplicaDetails(
                availability_domain=InputData_VM.blockvolreplica_availability_domain,
                display_name=blkvolocid['blockvolreplica_name'][i])]
                )
    )
    create_blockvol_data = create_volume_response.data
    #checking for the block volume activation status
    get_volume_response = core_client.get_volume(volume_id=create_blockvol_data.id)
    get_blockvol_data = get_volume_response.data

    while get_blockvol_data.lifecycle_state != "AVAILABLE":
        time.sleep(10)
        get_volume_response = core_client.get_volume(volume_id=create_blockvol_data.id)
        get_blockvol_data = get_volume_response.data
        print('Block Volume created from BlockVolumeReplica with id:',get_blockvol_data.id,'with status:',get_blockvol_data.lifecycle_state)
    
    # attach block volume to VM
    core_client1 = oci.core.ComputeClient(config)

    attach_volume_response = core_client1.attach_volume(
        attach_volume_details=AttachVolumeDetails(
            type=InputData_VM.block_vol_attachment_type,
            instance_id=getinst_data.id,
            volume_id=get_blockvol_data.id))
    print('Attached Block Volume to VM')
