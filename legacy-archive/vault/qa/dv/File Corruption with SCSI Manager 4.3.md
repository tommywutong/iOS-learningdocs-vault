---
title: File Corruption with SCSI Manager 4.3
apple_id: DTS10001147
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv06.html
archived_at: '2026-07-18T02:29:25.608304Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV06File Corruption with SCSI Manager 4.3 |

|  |
| --- |
| ---   Q: We are using SCSI Manager 4.3 on a Quadra 840. When SCSI Manager 4.3 is active (resident in the Extensions folder), we are experiencing a lot of problems -- mostly system hangs and data corruption in files. We ran tests to isolate these problems, using a variety of scenarios. In all the scenarios, the problems only occurred when SCSI Manager 4.3 was active.  When file corruption occurs, it is always in the first 16 bytes of a disk block. This area is overwritten by data that belongs in another area which is in offset 4096 bytes (400H) before the damaged area.  Is this a known problem, and if so, is there an update or patch for SCSI Manager 4.3?  A: This bug was identified and has been fixed in System 7.5.1 (System 7.5 with the update).  If a device goes bus-free after the command phase, the SCSI Manager 4.3 crashes. With the System 7.5 update applied, the SCSI Manager does not dispatch the next command if the bus is free after the earlier command. Also, SCSI Manager 4.3 in System 7.5 mistakenly tries to optimize TIBs on machines that do not have DMA, which could potentially cause data loss. TIB optimization is now turned off for pseudo-DMA machines.  For more information, see also:[Technote OS 07](https://developer.apple.com/library/archive/technotes/os/os_07.html). |

#### [Jul 01 1995]

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
