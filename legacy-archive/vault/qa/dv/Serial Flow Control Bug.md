---
title: Serial Flow Control Bug
apple_id: DTS10001169
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-03-14'
source_url: https://developer.apple.com/library/archive/qa/dv/dv28.html
archived_at: '2026-07-18T02:29:26.853273Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Serial](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSerial-date.html)

|  |
| --- |
| Technical Q&A DV28Serial Flow Control Bug |

|  |  |
| --- | --- |
| ---   Q: I'm calling the serial driver to clear XON/XOFF flow control but flow control is not being lifted. What's going on?  A: You have stumbled across a bug in Apple system software (ID 1635221). The File System Manager patches `_Control` in such a way that the `serdClrXOff` (csCode = 22) is mistaken for a block device "Return Media Icon" (csCode = 22) call. This causes the `serdClrXOff` to never make it to the serial driver.  The simplest workaround is to clear `ioVRefNum` before making the `serdClrXOff` call. The following code snippet demonstrates this technique.   |  | | --- | | ``` OSErr DoClearXOff(short serialOutDrvrRefNum) {   CntrlParam pb;   pb.ioCRefNum = serialOutDrvrRefNum;   pb.csCode = serdClrXOff;   pb.ioVRefNum = 0;   // This above line is required because of a bug   // in system software. The workaround, clearing   // ioVRefNum, should be benign when the bug is fixed   // in future systems.   return ( PBControlSync( (ParmBlkPtr) &pb ) ); } ``` |    This bug was fixed in Mac OS 8.0. |

#### [Jul 11 1997]

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
