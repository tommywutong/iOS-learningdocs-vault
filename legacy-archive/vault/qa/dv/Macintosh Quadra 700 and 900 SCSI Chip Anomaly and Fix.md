---
title: Macintosh Quadra 700 and 900 SCSI Chip Anomaly and Fix
apple_id: DTS10001149
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv08.html
archived_at: '2026-07-18T02:29:25.710184Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV08Macintosh Quadra 700 and 900 SCSI Chip Anomaly and Fix |

|  |  |
| --- | --- |
| ---   Q: Every now and then, my optical driver's Test Unit Ready command, which goes through the SCSI Manager, returns zero on the status byte, but two on the message byte. This is strange, because there's no cartridge inserted. Is something wrong with the SCSI Manager?  A: There is an identified problem in the SCSI chip on the Macintosh Quadra 700 and 900. The National 53c96 chips used in these models do something the SCSI Manager doesn't expect -- they sometimes retain a byte in the chip's onboard FIFO. As a result (in some cases), the SCSI Manager retrieves the stuck byte as the Status byte, and the Message byte as the Status byte, instead of retrieving the Status and Message bytes from the drive it just posted a command to.  Odd things may happen as a result of this anomaly. For instance, some users report that they can't get CD-ROM drives to work with Macintosh Quadra 900s, and some users also find that, periodically, they get "Can't read drive X" messages on the desktop.  The problem occurs with CD-ROM drives and other removable-media devices, such as SyQuest drives. Since these devices may or may not have media inserted, their drivers typically poll devices that don't have media inserted, looking for newly inserted media. Often, they do this by issuing a `TestUnitReady` SCSI command to the device. If the device returns a zero, which indicates NO ERROR, it's assumed that some sort of media is in the drive, so the driver tries to mount the newly inserted media.  This is the command sent to the CD-ROM drive:   |  | | --- | | ```   0, 0, 0, 0, 0, 0   |  |  |  |  |  |   |  |  |  |  | - Linked command byte: On Macintosh systems, always 0   |  |  |  | -  -  Reserved   |  |  |  -  -  -  Reserved   |  |  -  -  -  -  Reserved   |   -  -  -  -  -  Logical unit number (usually 0)     -  -  -  -  -  -  SCSI command: TestUnitReady ``` |   The last byte (SCSI command such as `Linked`) is always zero, and this is the byte that sticks in the `FIFO` of the c96, so when you read the Status and Message bytes back, you get a zero back as the Status byte, and a "Not Ready" (2) in the Message byte. Unfortunately, zero is the value returned to the driver, which proceeds to issue (in the case of the CD-ROM drive) a `_PostEvent`. This causes other `_Read` trap calls, all of which fail, and you end up with the Uninitialized Disk dialog box.  Apple has implemented a SCSI Manager fix for this problem in System 7.1 and later. |

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
