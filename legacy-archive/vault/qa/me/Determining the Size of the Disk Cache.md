---
title: Determining the Size of the Disk Cache
apple_id: DTS10001408
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-07-03'
source_url: https://developer.apple.com/library/archive/qa/me/me04.html
archived_at: '2026-07-18T02:29:43.715823Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A ME04Determining the Size of the Disk Cache |

|  |  |
| --- | --- |
|  Q: How do I determine the size of the Disk Cache set from the Memory Control Panel?  A: The disk cache is currently (System 7) stored in the SysParmType record, which you can retrieve with the `GetSysPPtr` call (documented in _Inside Macintosh:Operating Systems Utilities_, chapter 7). The misc field contains the size of the disk cache in 32K chunks stored in bits 8-15.  You can access this information using code such as:     |  | | --- | | ``` #include <OSUtils.h>  short GetDiskCacheSize(void) {     SysPPtr pramPtr;     short diskCacheSize;      pramPtr = GetSysPPtr();      diskCacheSize = ( ((unsigned short)(pramPtr->misc)) >> 8 ) * 32;         /* diskCacheSize is now the size in K of the disk cache */      return(diskCacheSize); } ``` |     [Jul 03 1996] |

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
