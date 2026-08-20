---
title: Detecting Classic and Carbon X Environments
apple_id: DTS10001510
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-10-16'
source_url: https://developer.apple.com/library/archive/qa/ov/ov03.html
archived_at: '2026-07-18T02:29:50.676120Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Runtime Architecture](https://developer.apple.com/library/archive/technicalqas/Carbon/idxRuntimeArchitecture-date.html) >

|  |
| --- |
| Technical Q&A OV03Detecting Classic and Carbon X Environments |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---      Q: My application does things that just won't work in the Classic environment. How do I detect the Classic environment so that I can tell the user why certain functionality has been disabled?  A: You can detect the Classic environment using `Gestalt`, as shown in Listing 1.   |  | | --- | | ``` // At the time of writing the latest version of Universal  // Interfaces was 3.3.2.  These definitions are not in UI 3.3.2, // but will be in the next release version.   enum {     gestaltMacOSCompatibilityBoxAttr = FOUR_CHAR_CODE('bbox'),                 /* Classic presence and features */     gestaltMacOSCompatibilityBoxPresent = 0,                                     /* True if running under the Classic */     gestaltMacOSCompatibilityBoxHasSerial = 1,                                   /* True if Classic serial support is implemented. */     gestaltMacOSCompatibilityBoxless = 2                                         /* True if we're Boxless (screen shared with                     Carbon/Cocoa) */ };   static Boolean RunningOnClassic(void) {     UInt32 response;          return (Gestalt(gestaltMacOSCompatibilityBoxAttr,                      (SInt32 *) &response) == noErr)                 && ((response &                      (1 << gestaltMacOSCompatibilityBoxPresent))                     != 0); } ``` | | __Listing 1__. Detecting whether you're running in the Classic environment. |   Q: My Carbon application does things on traditional Mac OS that just won't work on Mac OS X. How do I detect that I'm running on Mac OS X so that I can do things the right way on that platform?  A: DTS recommends that you test for specific functionality rather than for an entire platform. For example, if your application needs access to non-Carbon APIs on traditional Mac OS, we recommend that you access those APIs using `GetSharedLibrary` and `FindSymbol`; if the `GetSharedLibrary` call fails, you don't have access to the functionality, regardless of the platform.  On the other hand, we recognize that in some cases there is no convenient functional test, and only a platform test is possible. In such cases, your Carbon application can detect whether it is running on Mac OS X using `Gestalt`, as shown in Listing 2.   |  | | --- | | ``` static Boolean RunningOnCarbonX(void) {     UInt32 response;          return (Gestalt(gestaltSystemVersion,                      (SInt32 *) &response) == noErr)                 && (response >= 0x01000); } ``` | | __Listing 2__. Detecting whether your Carbon application is running on Mac OS X. | |

#### [Jan 16 2001]

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
