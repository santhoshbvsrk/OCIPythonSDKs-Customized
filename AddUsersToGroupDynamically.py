# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import InputData
import Output_01
from datetime import datetime
import os

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()
srch_strng="oracleidentitycloudservice/"

# Initialize service client with default config file
identity_client = oci.identity.IdentityClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_users_response = identity_client.list_users(
    compartment_id=InputData.tenancy_id)

# Get the data from response
for each_user in list_users_response.data:
    if srch_strng in each_user.name:
        add_user_to_group_response = identity_client.add_user_to_group(
            add_user_to_group_details=oci.identity.models.AddUserToGroupDetails(
            user_id=each_user.id,
            group_id=InputData.GroupOCID))

os.remove("06JunOutput_01.py") #using this as when I run this script from CMD Prompt I'll write the run time to a file, which I'm deleting before recreating it.
print("LastRunTime='",datetime.now(),"'")