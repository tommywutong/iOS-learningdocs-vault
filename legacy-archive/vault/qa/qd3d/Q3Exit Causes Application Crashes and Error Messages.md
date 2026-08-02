---
title: Q3Exit Causes Application Crashes and Error Messages
apple_id: DTS10001816
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d18.html
archived_at: '2026-07-18T02:38:40.159076Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD3D18Q3Exit Causes Application Crashes and Error Messages |

|  |
| --- |
|  Q: I'm trying to use the `kQ3RendererTypeInteractive` renderer, but it crashes frequently. If I run the program until just before the call to `Q3View_StartRendering`, and then click the close box of one of my MetroWerks debugger windows, there is an unrecoverable system crash. `Q3Exit` always causes the application to crash, sometimes with a message that a `Draw` context object still has one reference.  A: It is normal for the debugger to display debug strings in QuickDraw 3D when you call `Q3Exit`. These messages indicate memory leaks and such. The messages, which are only displayed with the debug version of the library, are there to let you know when your code may be causing a memory leak. There is a sample error and warning handler on AppleLink that you could modify to direct the message output to a file, thus avoiding the drops to MacsBug.  One way to avoid these messages is to call `Q3Object_Dispose` on any object that was created with a `Q3xxxx_Getxxxx` or `Q3xxx_Newxxx` call. |

#### [Jun 01 1995]

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
