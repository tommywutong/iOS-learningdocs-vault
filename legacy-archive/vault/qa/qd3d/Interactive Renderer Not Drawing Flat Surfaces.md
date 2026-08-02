---
title: Interactive Renderer Not Drawing Flat Surfaces
apple_id: DTS10001803
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d05.html
archived_at: '2026-07-18T02:38:39.351584Z'
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
| Technical Q&A QD3D05Interactive Renderer Not Drawing Flat Surfaces |

|  |
| --- |
|  Q: The Interactive renderer does not draw flat surfaces that are parallel to the camera-view direction with the Orthographic camera, but the wire-frame renderer does. We put in a "floor" of polygons, and when we look along the edge of the floor with the Orthographic camera, it totally disappears. With the wire-frame renderer, we see a line where the floor is, which is as expected.  A: Filled primitives have no thickness, so when you look at them edge-on, they do not appear. Lines, however, are a mathematical abstraction, so they always appear to be 1 pixel thick (when you "zoom in" on a line, its thickness does not increase). While this may seem somewhat odd, it is the way that many libraries work. To achieve the effect you want, make the "floor" a thin box, and texture-shade the top surface. If the depth of the box is small, it appears to be a slab-like structure, and it won't disappear. |

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
