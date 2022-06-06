#Create Multiple BlockVolumes
multibv_BlockVol_Name =["PythonSDK_BlockVol_02","PythonSDK_BlockVol_03","PythonSDK_BlockVol_04"]
multibv_compartmentid=""
multibv_AD="VPLM:PHX-AD-1"

#Attach Multiple Block Volume Input Data -- AttachMultipleBlockVolume.py
inst_vol_ocid = {'instance_ocid' : ['','',''],
              'volume_ocid' : ['','',''],
              'type' : ['iscsi','iscsi','iscsi']}

#Detach Multiple Block Volume Input Data -- DetachMultipleBlockVolume.py
volattach_id = ["ocid1.volumeattachment.","ocid1.volumeattachment.","ocid1.volumeattachment."]

#Delete Multiple BlockVolumes
multibv_vol_ids =['ocid1.volume.','ocid1.volume.','ocid1.volume.']

#Assign Users to Group
GroupOCID = 'ocid1.group.'
tenancy_id='ocid1.tenancy.'