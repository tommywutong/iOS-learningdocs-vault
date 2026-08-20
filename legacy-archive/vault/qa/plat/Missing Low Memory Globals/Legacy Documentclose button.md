---
title: Missing Low Memory Globals
apple_id: DTS10001537
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-01-09'
source_url: https://developer.apple.com/library/archive/qa/plat/plat27.html
archived_at: '2026-07-18T02:29:53.494986Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A PLAT27Missing Low Memory Globals |

|  |  |  |
| --- | --- | --- |
| ---   Q: I am getting a link error on my PowerPC application when I use the following low memory globals:   |  | | --- | | ``` 	LMGetHighHeapMark 	LMGetROMMapHandle 	LMGetStackLowPoint 	LMGetUnitTableEntryCount 	LMSetHighHeapMark 	LMSetROMMapHandle 	LMSetStackLowPoint 	LMSetUnitTableEntryCount ``` |   What is wrong? Is there a workaround?  A: Unfortunately, these globals didn't make it into the Interface library on PowerPC machines. This problem was discovered after InterfaceLib was frozen and in ROM. We are aware of the problem and it has been reported as a bug. The problem is that InterfaceLib is in ROM, so it's not as simple as shipping a new replacement library.  There is no good solution, but there is a workaround:  Create an external function in a file (say Extra.c) to access the low-mem yourself (from native code only), as shown below. When an updated library is released, you only have to remove the Extra.c.o file from your link command and relink your app, not recompile it.  Using `LMGetUnitTableEntryCount` as an example:   |  | | --- | | ``` // File: Extra.c // Add Extra.c.o to your PPCLink command line // Later, when a .xcoff file is provided by Apple, replace it with that, // and delete your Extra.c.o. file. #if defined(powerc) || defined (__powerc) pascal short LMGetUnitTableEntryCount() { 	return *(short *)0x01D2; } #endif ``` | |

#### [Jan 09 1997]

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
