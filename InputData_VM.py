#initializing variables
#Generic Fields
subnet_id="ocid1.subnet."
availability_domain="VPLM:AP-MUMBAI-1-AD-1"
compartment_id="ocid1.compartment."
is_auto_tune_enabled = True

#Boot Volume related fields
boot_vol_replica_id = "ocid1.bootvolumereplica."
create_boot_type = "bootVolumeReplica"
boot_vol_name = "<BootVolumeName>"
boot_vol_size_in_gbs = <BootVolumeSizeInGB>
boot_vol_vpus_per_gb = <VolumePerformanceUnitsInGB>
bootvolreplica_availability_domain = '<ReplicaRegionAD>'
bootvolreplica_name = '<BootVolumeReplicaName>'

#Block Volume related fields
block_vol_replica_id = "ocid1.blockvolumereplica."
block_vol_attachment_type = "iscsi"
block_vol_name = "<BlockVolumeName>"
blockvol_vpus_per_gb = <BlockVolumeSizeInGB>
blockvol_size_in_gbs = <VolumePerformanceUnitsInGB>
blockvolreplica_availability_domain = '<ReplicaRegionAD>'
blockvolreplica_name = '<BlockVolumeReplicaName>'

#Compute related fields
vm_display_name="<Compute/VM/Instance Name>"
vm_shape="<Compute/VM/Instance Shape>"
#if creating VM with Flex shapes, please provide the details of OCPUs & Memory
vm_ocpus=<ComputeOCPUs>
vm_memory_in_gbs=<ComputeMemory>
vm_assign_public_ip=<True/False>
vm_private_ip="<privateIPforYourVM>" #this is optional and is to be populated if you want the same IP for VM which you are creating from BootVol
