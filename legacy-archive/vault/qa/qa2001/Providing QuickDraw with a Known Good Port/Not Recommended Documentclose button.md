---
title: Providing QuickDraw with a Known Good Port
apple_id: DTS10002292
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2003-09-29'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1237.html
archived_at: '2026-07-18T02:38:20.382429Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/GraphicsImaging/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/GraphicsImaging/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > Carbon](https://developer.apple.com/referencelibrary/GraphicsImaging/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A QA1237Providing QuickDraw with a Known Good Port |

|  |
| --- |
| ---   Q: How do I provide QuickDraw with a known good port?  A: In many cases, you need to dispose of the object (`GWorldPtr`, `CGrafPtr`, etc.) that is the current port. However, you should never leave QuickDraw with an invalid current port so you must always set the current port to a known good port before disposing of the object. The real question is, what do you do if you don't have a known good port to set?  Before Carbon and Mac OS X, you could set the current port to the Window Manager port (via `LMGetWMgrPort`) in order to leave QuickDraw in a valid state. However, under Carbon, the Window Manager port is no longer available. In addition, QuickDraw on Mac OS X is even pickier about having a valid port due to the use of protected memory.  Thankfully, as of Mac OS X 10.1, QuickDraw provides a simple solution: call `SetPort( NULL )`. `SetPort( NULL )` on Mac OS X 10.1 and later has the useful semantic of setting the current port to a "fallback port" which will prevent crashes due to bad dereferences but has an empty bounds to prevent unwanted drawing. This is very similar to the behavior that the Window Manager has had for years. Since Mac OS 8.5 (and still present in Mac OS X), the Window Manager has automatically set the port to a scratch port whenever you destroy the window containing the current port.  Please note that the `SetPort( NULL )` semantic is not supported on Mac OS 9, even for Carbon applications.   ---  [Sep 29, 2003] |

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
