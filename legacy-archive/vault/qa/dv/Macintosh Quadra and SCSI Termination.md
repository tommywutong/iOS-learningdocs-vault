---
title: Macintosh Quadra and SCSI Termination
apple_id: DTS10001150
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv09.html
archived_at: '2026-07-18T02:29:25.776188Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV09Macintosh Quadra and SCSI Termination |

|  |
| --- |
| ---   Proper SCSI termination is critical for correct operation of all Macintosh computers. The Macintosh Quadra computers require external SCSI termination at the end of the device chain, which should be supplied either by the last device in the chain, or by a standard Apple SCSI Cable Terminator (M0332LL/A). Note that this is the standard SCSI terminator and _not_ the black terminator required by the Mac IIfx (the black IIfx terminator may also be used).  Termination is generally supplied at the factory for use with internal SCSI devices. Some early floppy-only Macintosh Quadra 700 units may not have internal termination, so users who attach external SCSI devices may need to double-terminate their external SCSI chain if they have not installed an internal SCSI device. Properly terminated floppy-only Macintosh Quadra 700 units have a terminator inserted into the motherboard's internal SCSI-cable connector. Users of internal SCSI devices must, of course, remove this terminator before connecting their internal SCSI device.  The Macintosh Quadra 900 is the first Macintosh computer to provide a separate, internal SCSI bus. This bus is physically isolated from the external SCSI bus and must also be properly terminated. The cable provided with the computer includes all the termination necessary, so _all_ internal devices must have SCSI termination removed before connecting to the internal Macintosh Quadra 900 SCSI cable. If extra termination is supplied, it may cause intermittent hardware failures as well as physical damage to the device.  Developers who ship terminated SCSI devices for possible internal use in the Macintosh Quadra 900 must provide users with instructions for removing the termination.  For more information, see also:[Technote DV 15 on SCSI Termination](https://developer.apple.com/library/archive/technotes/dv/dv_15.html). |

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
