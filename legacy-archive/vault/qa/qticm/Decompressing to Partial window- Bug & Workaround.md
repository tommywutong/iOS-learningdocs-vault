---
title: 'Decompressing to Partial window: Bug & Workaround'
apple_id: DTS10001931
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qticm/qticm12.html
archived_at: '2026-07-18T02:38:45.937632Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > QuickTime](https://developer.apple.com/referencelibrary/QuickTime/index.html)

|  |
| --- |
| Technical Q&A QTICM12Decompressing to Partial window: Bug & Workaround |

|  |
| --- |
| Q Under System 7, decompressing directly to a window that is partially "off the screen" (that is, not completely visible) results in a -50 (invalid param) QuickTime error. We can special case when windows are off the screen and decompress into an offscreen GWorld but we would prefer a fix to either QuickTime or System 7.   A The problem you are having is due to a bug in the Image Compression Manager. It fails to clear QDError when starting a decompression job and later checks it to see if it is OK to continue the operation. Something else is setting QDErr and your call fails. The solution that you can implement now consists of clearing QDErr before calling any of the decompression routines. You can accomplish this by calling QDError (which clears the error after it passes the current value to you) or zeroing the low mem QDerr (0xD6E) by hand.  Future versions of QuickTime will have the fix and will not require that you work around the problem. [May 01 1995] |

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
