---
title: Using Windows GDI for all drawing
apple_id: DTS10002166
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qtw/qtw98.html
archived_at: '2026-07-18T02:38:53.446439Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [QuickTime for Windows](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxQuickTimeforWindows-date.html) >

|  |
| --- |
| Technical Q&A QTW98Using Windows GDI for all drawing |

|  |
| --- |
| ---   Q: I'd like to tell QuickTime for Windows to use the Windows Graphics Device Interface (GDI) for all drawing in my application, rather than the DirectDraw or DCI services. How can I do this?  A: Use the QuickTime for Windows `InitializeQTML` function, specifying the `kInitializeQTMLUseGDIFlag` flag. The `InitializeQTML` function is used to initialize the QuickTime Media Layer, which you must do before your program can perform any QuickTime operations. [Sep 05 2000] |

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
