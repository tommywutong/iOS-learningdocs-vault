---
title: Detecting a CD-ROM
apple_id: DTS10001159
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-01-31'
source_url: https://developer.apple.com/library/archive/qa/dv/dv18.html
archived_at: '2026-07-18T02:29:26.216704Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [Storage](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxMassStorageDevices-date.html) >

|  |
| --- |
| Technical Q&A DV18Detecting a CD-ROM |

|  |  |  |
| --- | --- | --- |
| ---   Q: My application runs from the hard disk, but it requires a specific CD-ROM to be present on the system. I am concerned about the possibility that a user may have a hard-disk volume or a diskette with the same name as my CD-ROM. To check for this, my application searches for a specifically named locked volume that contains a certain file, and I'd like to simplify this process. What is the best way to determine if a mounted volume or SCSI address is a CD-ROM drive?  A: In the past, there was no foolproof way to determine whether a drive on the Macintosh is a CD-ROM, so developers tried several methods:   1. Inspect the drive-queue element for a mounted drive to determine which    driver the `dQRefNum` points to. Then, inspect    the driver's name. If the name is ".AppleCD", it's probably a CD-ROM drive. 2. This approach fails for non-Apple CD-ROM drives, since they have different    driver names. 3. Inspect the drive's attributes in the four bytes preceding the    drive-queue entry. If the drive is "locked in hardware" and    is removable, it's probably a CD-ROM drive. 4. Issue a SCSI request directly to the drive. 5. This fails for some early CD-ROM drives (non-SCSI-2 compliant). Before    SCSI-2, there was no CD-ROM device type defined, and some CD-ROM drives    reported that they were hard disks. There is an additional complication    introduced by SCSI Manager 4.3, and IDE CD-ROM drives require a completely    different calling architecture. 6. Furthermore, some newer Macintosh models such as the PowerBook 1400 and many of the    clones use an ATAPI protocol-based CD-ROM drive and therefore won't show up    in any SCSI probing you do.   However, since the introduction of version 5.2.X. of the .AppleCD (and any .AppleCD compliant) driver, CD-ROM drivers have supported the `DriverGestalt` csCode.  To find the inserted CD-ROM drives using these drivers, you can scan the Drive Table and issue `DriverGestalt` commands to the drivers to determine the device type. The following snippet will illustrate this:   |  | | --- | | ``` #include <DriverGestalt.h> void FindTheCD-ROMS(void)                   //  Scan Drive table for CD-ROMS {     DriverGestaltParam          pb;     DrvQEl  *dqp;     OSErr   status;     pb.csCode       = kDriverGestaltCode;       // Setup Driver Gestalt PB     pb.driverGestaltSelector = kdgDeviceType;   // ask for Device Type     dqp = (DrvQEl *) GetDrvQHdr()->qHead;   // Start with head of drive queue      while (dqp != NULL) {                   // for each device in drive queue         pb.ioCRefNum    = dqp->dQRefNum;            // Get the driver refNum         pb.ioVRefNum    = dqp->dQDrive;             // get the drive  refNum         status = PBStatusSync((ParmBlkPtr) &pb);    // Do a Driver Gestalt call         if (status == noErr)             if(pb.driverGestaltResponse == kdgCDType ) // Device type is 'cdrm'             {                     printf("Drive: %d Driver:(%d) ",                              (int) dqp->dQDrive, dqp->dQRefNum);             }         dqp = (DrvQEl *) dqp->qLink;                // Next drive     } } ``` |   A complete sample entitled [Macintosh Disk Driver Gestalt Sample](http://www.vmeng.com/vinnie/Papers/DriverGestaltDemo.html) is available from DTS which illustrates how to query devices.  To discover any unmounted drives, you need to use either the SCSI or ATA manager, whichever is appropriate. The ['ATA demo' DTS code sample](http://www.vmeng.com/vinnie/Papers/ATADemo.html) illustrates how to scan the ATA bus and identify the available devices.  There is also a driver `Status` call for available on the .AppleCD driver starting in version 5.2.X. that will return information on the type of CD-ROM device.  Issue a Status Call to the .AppleCD Driver with the following parameters:   |  | | --- | | ```     csCode = 120     csParam[ 0 -1]   will return a DeviceIdent of the form typedef struct DeviceIdent{   uchar busType;                // SCSI -  0                ATAPI = 7   uchar bus;                    // SCSI - Bus#              ATAPI = 0   uchar targetID;               // SCSI - Target SCSI ID    ATAPI = Bus #   uchar partition ;             // SCSI - LUN               ATAPI  = 0 } ``` |   One thing to note: if you are using an older version of the .AppleCD driver, the above calls might not work, in which case you may consider either falling back to previous methods or requesting the user update their CD-ROM driver. |

#### [Jan 31 1997]

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
