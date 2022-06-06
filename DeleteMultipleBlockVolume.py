import oci
import InputData

config = oci.config.from_file()
core_client = oci.core.BlockstorageClient(config)

for blockVol_Ids in InputData.multibv_vol_ids:
    delete_volume_response = core_client.delete_volume(volume_id=blockVol_Ids)
    # Get the data from response
    print(delete_volume_response.headers)