# Customizing OCI Python SDKs!

This repo contains OCI Python SDKs which are enhanced for specific requirement on top of the Oracle Provided Python SDKs

 - **InputData.py** --> We will be passing all input values to respective Python SDKs through this, so that we need not touch the main code file.  
   
 - **AddUsersToGroupDynamically.py** --> This file helps you list all the users in tenancy and move all IDCS users only to a specific Group. You can update this file by changing condition to filter out specific users based on some search criteria and move them to a Group. You can also enhance this to move only new users to a specific
Group by adding date condition.

 - **AttachMultipleBlockVolume.py** --> This file helps you to attach multiple block volumes to different Compute instances in a single call.
 
 - **DeleteMultipleBlockVolume.py** --> This file helps to delete multiple block volumes in a single call.

 - **DetachMultipleBlockVolume.py** --> This file helps in detaching multiple Block Volumes attached to different Compute instances in a single call.

 - **createMultipleBlockVolume.py** --> This file helps in creating Multiple Block Volumes in a single call.

 - **createMultipleBlockVolume.py** --> This file helps in listing and deleting multiple compute instances at a time from a specific compartment & availability domain.

 - **createVMFromBootVolAndAttachBlockVol.py** --> This file helps in creating a Virtual Machine from Boot Volume and attaching a Block Volume to it.

 - **ActivateBootBlockReplicas_CreateVM_AttachBlockVolume.py** --> This file completes the below steps in a single click:
      1.	Create Boot Volume from BootVolumeReplica in DC/DR.
      2.	Create Block Volume from BlockVolumeReplica in DC/DR.
      3.	Create VM/Compute/Instance in DC/DR from the Boot Volume created in Step1.
      4.	Attach the Block Volume created in Step2.



## NOTE

 - [ ] You can further enhance these by not feeding in the data manually
       and rather take from output of another SDK call output. 
       
 - [ ] You can also enhance it by making multiple SDK calls via a single
       Python
              call i.e., creating Multiple Block Volumes and attaching them to
              specific compute instances.
