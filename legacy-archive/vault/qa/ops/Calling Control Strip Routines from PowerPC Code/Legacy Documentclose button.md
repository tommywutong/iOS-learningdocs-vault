---
title: Calling Control Strip Routines from PowerPC Code
apple_id: DTS10001496
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-03-14'
source_url: https://developer.apple.com/library/archive/qa/ops/ops15.html
archived_at: '2026-07-18T02:29:49.661215Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS15Calling Control Strip Routines from PowerPC Code |

|  |
| --- |
| Q I'm trying to call the routines `SBIsControlStripVisible()` and `SBShowHideControlStrip()` defined in the header file `<ControlStrip.h>`. When I try to link the PowerPC code, I get a link error on these routines. Which library are they implemented in?   A There is no PowerPC library for Control Strip calls. As a consequence, you must create a routine descriptor and perform a Mixed Mode call to the 68K library. The following is an example of how you can call the Control Strip routines from PowerPC code:   ``` /* Defined in current Universal Header */  #ifndef _ControlStripDispatch enum {     _ControlStripDispatch = 0xAAF2 }; #endif  #if GENERATINGCFM  /*  */ /*  If we're not generating CFM, then assume the */ /*  68K inlines in the headers apply instead. */ /*  */  #include <MixedMode.h> #include <OSUtils.h> pascal Boolean SBIsControlStripVisible ( void ); pascal void SBShowHideControlStrip(Boolean showIt);  /*  SBIsControlStripVisible is a Pascal routine, */ /*  dispatched from the selector in D0, returning */ /*  a Boolean result */ pascal Boolean SBIsControlStripVisible ( void ) {     enum         {         uppSBIsControlStripVisibleInfo = kD0DispatchedPascalStackBased             | RESULT_SIZE (SIZE_CODE (sizeof(Boolean)))             | DISPATCHED_STACK_ROUTINE_SELECTOR_SIZE (kFourByteCode)             };              return CallUniversalProc (             GetToolTrapAddress (_ControlStripDispatch),             uppSBIsControlStripVisibleInfo, 0x00); }  pascal void SBShowHideControlStrip(Boolean showIt) {     enum         {         uppSBShowHideControlStripInfo =             kD0DispatchedPascalStackBased             | DISPATCHED_STACK_ROUTINE_SELECTOR_SIZE (kFourByteCode)             | DISPATCHED_STACK_ROUTINE_PARAMETER                 (1, SIZE_CODE (sizeof (showIt)))             };              CallUniversalProc (             GetToolTrapAddress (_ControlStripDispatch),             uppSBShowHideControlStripInfo, 0x01, showIt); }  #else   /*  not GENERATINGCFM */ #include <ControlStrip.h> #endif /*  GENERATINGCFM */ ```    Updated: 14-March-97 |

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
