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

inst_id = InputData.inst_ocid

# Send the request to service, some parameters are not required, see API
# doc for more info

for i in range(len(inst_id['instance_ocid'])):
    terminate_instance_response = core_client.terminate_instance(
        instance_id= inst_id['instance_ocid'][i],
        preserve_boot_volume=False)

# Get the data from response
print(terminate_instance_response.headers)
