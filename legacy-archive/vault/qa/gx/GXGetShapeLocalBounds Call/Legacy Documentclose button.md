---
title: GXGetShapeLocalBounds Call
apple_id: DTS10001207
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gx/gx02.html
archived_at: '2026-07-18T02:29:30.738275Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GX02GXGetShapeLocalBounds Call |

|  |
| --- |
| ---   Q: The `GXGetShapeLocalBounds` call is causing many problems for us. According to the documentation, `GXGetShapeLocalBounds` should not have to use the viewport, and that it should just compute the geometry after the mapping to get the shape in local coordinates, but it does seem to use the viewport for the gxPicture.  A: If the transform for the picture is the same as the view transform (before the view is disposed), the behavior you're seeing is as-expected. This is because you're referencing a field of a disposed object, which would contain garbage.  `GXGetShapeLocalBounds` are not completely reliable for pictures, because you cannot tell what the transform for all of the objects within a picture is. Each object in the picture may have a transform set, and/or you may have nested objects (in the case of a picture within a picture). The `GXGetShapeLocalBounds` function returns the bounding rectangle of the source shape after the shape's transform mapping and style are applied. The dimensions of the rectangle are in the shape's local coordinates.  Try using the `GXGetShapeBounds` function to determine the bounding rectangle of a shape or of a specified contour of a shape. To get this in the same form that `GXGetShapeLocalBounds` returns, get the transform mapping and apply it to the shape.  To do this, make the following sequence of calls:   - Use the `GXGetShapeTransform` function to determine the transform object associated with a shape object. - Examine the mapping property of a transform object directly using the function `GXGetTransformMapping`.   Once you have the transform-mapping matrix, you can transform the bounds returned by `GXGetShapeBounds`. This may seem like a roundabout way of doing this, but it is the best way to avoid the problems you're having. Bear in mind that you may need to iterate through the picture to get the bounds of all of its component objects. |

#### [Mar 05 1996]

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
