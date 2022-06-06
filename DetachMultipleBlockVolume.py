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

vol_attachid = InputData.volattach_id

# Send the request to service, some parameters are not required, see API
# doc for more info
for x in vol_attachid:
    detach_volume_response = core_client.detach_volume(
        volume_attachment_id=x)
    
    # Get the data from response
    print(detach_volume_response.headers)