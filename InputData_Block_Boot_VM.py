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
boot_vol_size_in_gbs = <BootVolumeSize>
boot_vol_vpus_per_gb = <BootVolumePerformanceUnits>
bootvolreplica_availability_domain = 'VPLM:AP-HYDERABAD-1-AD-1'
bootvolreplica_name = '<BootVolumeReplicaName>'

#Block Volume related fields
block_vol_replica_ocid = {'block_vol_name' : ['<BlockVolumeName>','<BlockVolumeName>','<BlockVolumeName>'],
                          'blockvol_vpus_per_gb' : [<BlockVolumePerformance>,<BlockVolumePerformance>,<BlockVolumePerformance>],
                          'blockvol_size_in_gbs' : [<BlockVolumeSize>,<BlockVolumeSize>,<BlockVolumeSize>],
                          'block_vol_replica_id' : ['ocid1.blockvolumereplica.','ocid1.blockvolumereplica.','ocid1.blockvolumereplica.'],
                          'blockvolreplica_name' : ['<BlockVolumeReplicaName>','<BlockVolumeReplicaName>','<BlockVolumeReplicaName>']
                          }
block_vol_attachment_type = "iscsi"
#block_vol_name = "<BlockVolumeName>"
#blockvol_vpus_per_gb = <BlockVolumePerformanceUnits>
#blockvol_size_in_gbs = <BlockVolumeSize>
blockvolreplica_availability_domain = 'VPLM:AP-HYDERABAD-1-AD-1'
#blockvolreplica_name = 'BlockVolReplica01'

#Compute related fields
vm_display_name="OCI_DR_VM_San"
vm_shape="VM.Standard3.Flex"
vm_ocpus=1
vm_memory_in_gbs=16
vm_assign_public_ip=False
vm_private_ip="10.0.1.10"

#Attach Multiple Block Volume Input Data -- AttachMultipleBlockVolume.py
inst_vol_ocid = {'instance_ocid' : ['','',''],
              'volume_ocid' : ['ocid1.volume.','ocid1.volume.','ocid1.volume.'],
              'type' : ['iscsi','iscsi','iscsi']}
