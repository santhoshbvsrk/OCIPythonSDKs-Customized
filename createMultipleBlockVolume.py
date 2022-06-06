import oci
import InputData

config = oci.config.from_file()
core_client = oci.core.BlockstorageClient(config)

for VolName in InputData.multibv_BlockVol_Name:
    create_volume_response = core_client.create_volume(
    create_volume_details=oci.core.models.CreateVolumeDetails(
        compartment_id=InputData.multibv_compartmentid, availability_domain=InputData.multibv_AD, display_name=VolName))
    print(create_volume_response.data)