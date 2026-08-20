---
title: RAVE Support for Apple 3D Accelerator
apple_id: DTS10001889
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-04-20'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d91.html
archived_at: '2026-07-18T02:38:45.237280Z'
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
| Technical Q&A QD3D91RAVE Support for Apple 3D Accelerator |

|  |
| --- |
| ---   Q: How do I make my application work with the Apple Hardware card?  A: Your best bet is to call QuickDraw 3D, since it does all the right things. However, here's a list of some of the pitfalls of the Apple Hardware card.   1. You must explictly enable the engine using `QAEngineEnable`. 2. You can only create deep-_z_ contexts, and must send triangles with correct _z_ information. 3. Texture modulation and highlighting are always turned on, so you must set the texture colors even if you aren't using those texture ops. 4. The Apple hardware supports either twelve (12) 128x128x32-bit textures, or three (3) 256x256x32-bit textures, per frame. Textures cannot be deleted to make additional room for more textures. If you don't need texture wrapping, you can put combine smaller textures in a single larger texture, and calculate the appropriate _u_ and _v_ coordinates to choose the smaller texture. 5. It can render either to a `GDevice` or to a Memory Device. This hardware can render in single-buffered mode without tearing, so creating single buffered contexts will improve performance.  [Apr 20 1998] |

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
