# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import InputData

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()

# Initialize service client with default config file
core_client = oci.core.ComputeClient(config)

inst_volid = InputData.inst_vol_ocid

for i in range(len(inst_volid['instance_ocid'])):
    attach_volume_response = core_client.attach_volume(
        attach_volume_details=oci.core.models.AttachIScsiVolumeDetails(
            type=inst_volid['type'][i],
            instance_id=inst_volid['instance_ocid'][i],
            volume_id=inst_volid['volume_ocid'][i]))
    
# Get the data from response
print(attach_volume_response.data)