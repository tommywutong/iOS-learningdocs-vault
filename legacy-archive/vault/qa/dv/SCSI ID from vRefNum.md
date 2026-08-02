---
title: SCSI ID from vRefNum
apple_id: DTS10001170
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-05-23'
source_url: https://developer.apple.com/library/archive/qa/dv/dv29.html
archived_at: '2026-07-18T02:29:26.913996Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Accessibility](https://developer.apple.com/referencelibrary/HardwareDrivers/idxAccessibility-date.html)

|  |
| --- |
| Technical Q&A DV29SCSI ID from vRefNum |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: I would like to obtain the SCSI-ID of a disk volume where a certain file is located. What is the way to do it?  A: I assume you've already thought ahead to the cases where the drive in question is not SCSI (e.g., floppy, IDE, RAM disk, etc.)  There are two answers to this question, depending upon whether SCSI Manager 4.3 is present or not. If SCSI Manager 4.3 is not present, you rely on the fact that SCSI devices are at a particular place in the unit table. To summarize _Inside Macintosh:Devices_, SCSI drivers go in slots 32-40 in the unit table in order, so the driver for SCSI 0 is in slot 32, SCSI 1 is in slot 1, etc.   |  | | --- | | ```      slot number = -(refnum-1) ``` |    So the driver for SCSI 0 has refnum -33, SCSI 1 has refnum -34, etc.  If SCSI Manager 4.3 is installed, you call the routine `SCSILookupRefNumXRef()` as documented in [Inside Macintosh:Devices on page 4-52 and 4-53](https://developer.apple.com/documentation/mac/Devices/Devices-185.html).  To detect the presence of SCSI Manager 4.3, check that the trap _SCSIAtomic is unimplemented, as demonstrated in [Inside Macintosh:Operating System Utilities on page 8-21 through 8-23](https://developer.apple.com/documentation/mac/OSUtilities/OSUtilities-171.html#HEADING171-5). You also want to read the "I Am Curious SCSI" note in the SCSI Samples 1.0 folder on the Tool Chest developer CD  Given that you have a volume reference number, you need to obtain the driver reference number. You get this by calling `PBHGetVInfo()`, documented in [Inside Macintosh:Files on page 2-144](https://developer.apple.com/documentation/mac/Files/Files-178.html).   |  | | --- | | ``` OSErr   GetDRefNumFromVRefNum(short vRefNum, short *dRefNum) {     HParamBlockRec  pb;     Str27           volName;     OSErr           result;      pb.volumeParam.ioVRefNum = vRefNum;     pb.volumeParam.ioNamePtr = volName;     pb.volumeParam.ioVolIndex = 0;  /* use ioVRefNum only,                                         return volume name */     result = PBHGetVInfoSync(&pb);     if (result == noErr)         *dRefNum = pb.volumeParam.ioVDrvInfo;     return result; } ``` |    Given the driver reference number, use the code below (from "I Am Curious SCSI").   |  | | --- | | ``` /*  * Get the SCSI Bus ID for a particular driver reference number. This is  * valid for the original SCSI Manager. Under the asynchronous SCSI Manager,  * it is needed if the driver did not register with the SCSI Manager.  */ #define DriverRefNumToSCSI(x)  ((signed short) (~(x) - 32))   /*  * Return the DeviceIdent for a particular driver by searching the list of  * registered devices. Return noErr on success, or nsvErr if there is none  */ OSErr DriverRefNumToDeviceID(         short        driverRefNum,         DeviceIdent  *deviceIdentPtr     ) {     OSErr            status, scsiStatus;     SCSI_DriverPB    pb;     short            targetID;      status = nsvErr;     if (AsynchronousSCSIManagerPresent()) {         /*          * Scan the list of registered drivers for          * this driverRefNum.          */         ClearMemory((ptr) &pb, sizeof pb);         pb.scsiPBLength = sizeof (SCSI_Driver_PB);         pb.scsiCompletion = NULL;         pb.scsiFlags = 0;         pb.scsiFunctionCode = SCSILookupRefNumXref;         /* Initialize the DeviceIdent to an          * "impossible" value to start the scan          * process. SCSIAction will return the          * current device in pb.scsiDevice and the          * next registered device in          * pb.scsiNextDevice. The do loop examines          * each registered device in turn. The loop          * exits when the next device is on an          * illegal bus. Note that the test must          * ignore the first value as the current          * bus (pb.scsiDevice.bus ) contains the          * "illegal" designation.          */           *((long *) &pb.scsiDevice) = -1L;          do {             scsiStatus = SCSIAction((SCSI_PB *) &pb);             if (scsiStatus != noErr) {                 status = scsiStatus;                 break;             }             if (pb.scsiDriver == driverRefNum /* Is this the driver we want? */              && pb.scsiDevice.bus != 0xFF) {  /* Is this a real bus? */                 *deviceIdentPtr = pb.scsiDevice;                 status = noErr;                 break;             }             pb.scsiDevice = pb.scsiNextDevice;         } while (pb.scsiDevice.bus != 0xFF);     }     if (status == nsvErr) {         /*          * The asynchronous SCSI Manager is missing or the          * driver didn't register with the SCSI Manager.*/         targetID = DriverRefNumToSCSI(driverRefNum);         if (targetID >= 0 && targetID <= 6) {             deviceIdentPtr->diReserved = 0;             deviceIdentPtr->diBus = 0;             deviceIdentPtr->targetID = targetID;             deviceIdentPtr->LUN = 0;             status = noErr;         }     }     return (status); } ``` | |

#### [May 23 1997]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
