---
title: Determining if a Drive is a Network Volume
apple_id: DTS10001187
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/fl/fl01.html
archived_at: '2026-07-18T02:29:28.500038Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > File Management](https://developer.apple.com/referencelibrary/Carbon/idxFileManagement-date.html)
- [Carbon > Networking](https://developer.apple.com/referencelibrary/Carbon/idxNetworking-date.html)
- [Carbon > Porting](https://developer.apple.com/referencelibrary/Carbon/idxPorting-date.html)
- [Darwin > Hardware & Drivers](https://developer.apple.com/referencelibrary/Darwin/idxHardwareDrivers-date.html)
- [Darwin > Networking](https://developer.apple.com/referencelibrary/Darwin/idxNetworking-date.html)
- [Hardware & Drivers > Ethernet](https://developer.apple.com/referencelibrary/HardwareDrivers/idxEthernet-date.html)
- [Hardware & Drivers > Networking](https://developer.apple.com/referencelibrary/HardwareDrivers/idxNetworking-date.html)
- [Hardware & Drivers > Storage](https://developer.apple.com/referencelibrary/HardwareDrivers/idxMassStorageDevices-date.html)
- [Internet & Web > Networking](https://developer.apple.com/referencelibrary/InternetWeb/idxNetworking-date.html)
- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)
- [Networking > Hardware & Drivers](https://developer.apple.com/referencelibrary/Networking/idxHardwareDrivers-date.html)
- [Porting > Carbon](https://developer.apple.com/referencelibrary/Porting/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A FL01Determining if a Drive is a Network Volume |

|  |  |
| --- | --- |
| ---   Q: If I have a physical drive ID, how can I determine if that drive is a network volume? I'm not sure where to look, and I need to know if the information is dependable and not subject to change.  A: Under the current Macintosh file system, there is no completely dependable way to determine if a volume originates over a network or is implemented on a local disk. This is the result of the way external file systems are implemented -- a third party can build a network file system in a variety of ways.  You can, however, easily determine if a volume utilizes the AFP (Appleshare) file system, which in most cases, is adequate. To make this determination, compare the drive-queue entry's driver refnum to the Appleshare client's refnum.  The following sample code enumerates the drive queue and displays the relevant information:   |  | | --- | | ``` main() {       QHdrPtr        DrvQHdr =  GetDrvQHdr();     DrvQElPtr    dqeP;     short        afpRefNum = 0;     OSErr        ErrNo; // Get the Driver refNum for AFP     ErrNo    = OpenDriver("\p.AFPTranslator",&afpRefNum); // Scan each drive in the Drive Table     dqeP = (DrvQElPtr)DrvQHdr->qHead;     do { // is it an AFP volume or SCSI device         if(dqeP->dQRefNum == afpRefNum) printf("AFP      ");     } while (dqeP =(DrvQElPtr) dqeP->qLink); } ``` |   For other third-party file systems, such as DECNET and NFS, you have to determine the name of their driver, and then compare it to the Appleshare client's refnum. |

#### [May 01 1995]

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
