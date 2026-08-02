---
title: Calling ataManager on a Power Macintosh
apple_id: DTS10001167
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-09-21'
source_url: https://developer.apple.com/library/archive/qa/dv/dv26.html
archived_at: '2026-07-18T02:29:26.647671Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > ATA](https://developer.apple.com/referencelibrary/HardwareDrivers/idxATA-date.html)

|  |
| --- |
| Technical Q&A DV26Calling ataManager on a Power Macintosh |

|  |  |
| --- | --- |
| ---   Q: We're working on drivers for the ATA bus in Power Macintosh computers. However, we can't seem to find the link libraries on our ETO disks. The header libraries are there, but there is nothing to link to.  A: Classic 68K code calls ATA Manager through inline trap glue and does not need a link library. CFM (PowerPC and CFM-68K) code needs to used Mixed Mode glue to call the `ataManager` trap. The following code should do:   |  | | --- | | ``` #include <MixedMode.h> #include <Patches.h> #include <ATA.h>   extern pascal SInt16 ataManager(ataPB *pb) {     return CallUniversalProc(                 GetToolboxTrapAddress(0xAAF1),                 kPascalStackBased                 | RESULT_SIZE(SIZE_CODE(sizeof(SInt16)))                 | STACK_ROUTINE_PARAMETER(1, SIZE_CODE(sizeof(pb))),                 pb); } ``` | |

#### [Sep 21 1998]

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
