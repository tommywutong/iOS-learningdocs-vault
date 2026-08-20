---
title: Detecting Control Strip at Startup
apple_id: DTS10001499
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-10-19'
source_url: https://developer.apple.com/library/archive/qa/ops/ops18.html
archived_at: '2026-07-18T02:29:49.837739Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS18Detecting Control Strip at Startup |

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Q Under Mac OS 8.5, when I call the Control Strip API at boot time the Mac crashes. I have verified that `ControlStripDispatch` is implemented. What is the source of the crash?   A Any extension calling the Control Strip software should be sure that the Control Strip exists and is loaded before it attempts to make any call to it. Just checking that `ControlStripDispatch` trap is implemented is insufficient. Starting with Mac OS 8.5, Control Strip is an application and is not loaded at startup time. Therefore extensions cannot make Control Strip calls (such as `SPBShowHideControlStrip`) at startup time. Calling Control Strip routines when Control Strip is not running will cause a crash.  The proper way for an application or extension to determine if it is safe to call Control Strip is to use `Gestalt` with the `gestaltControlStripAttr` selector and check that the `gestaltControlStripExists` bit is set, which indicates that Control Strip and its complete API is available. The following code shows how to do this: |  |  | | --- | | ``` static Boolean IsControlStripAvailable (void) {     OSStatus err;     long response;      err = Gestalt (gestaltControlStripAttr, response);     if (response & (1 << gestaltControlStripExists)) {         // It is safe to call Control Strip         return true;     } else {         // It is not safe to call Control Strip         return false;     } } ``` |    Updated: 19-Oct-98 |

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
