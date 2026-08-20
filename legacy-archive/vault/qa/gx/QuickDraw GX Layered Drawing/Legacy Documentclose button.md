---
title: QuickDraw GX Layered Drawing
apple_id: DTS10001209
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gx/gx04.html
archived_at: '2026-07-18T02:29:30.906621Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GX04QuickDraw GX Layered Drawing |

|  |
| --- |
| ---   Q: Our application has multiple shapes layered on top of each other. The bottom object is a graphic, and the objects on top of it are text shapes. The text objects are transparent, permitting the underlying graphic to show through.  Are there functions in GX to facilitate refreshing the background shapes when characters are deleted in the text-layout shapes above it? We need to refresh the graphic with minimal flicker and want to avoid resorting to the standard `Copybits` function.  A: QuickDraw GX does not have any direct functions to facilitate refreshing or redrawing shapes that are drawn on top of each other, such as updating only a portion of a shape. However, there are a few methods that can be used in conjunction with various GX and QuickDraw calls to accomplish your goals. Here are three approaches you could use:   1. You can use the standard `CopyBits` function to update the appropriate area. You can have GX draw directly into a QuickDraw GWorld. This approach works if you need to draw QuickDraw and GX objects in the same window. 2. If you merge multiple GX shapes into a GX picture, you can use the picture's clip shape to update the area in question. With GX pictures, you can collect all of your shapes into a GX picture with your graphic shape as the bottom shape within the GX picture's hierarchy. This forces GX to draw the graphic as the first shape, with your other multiple shapes drawn on top.  GX pictures are smart, in the sense that GX draws only the shapes which are    visible for the clip shapes associated with the picture and all of the shapes    contained within the picture. A clip shape within GX can be any geometric shape    (path, polygon, rectangle, or curve).  To update the smallest possible area, determine the QuickDraw update region,    and convert it to a GX path. Next, get the current clip shape of the picture    with `GXGetShapeClip` (..), thereby making it possible to restore the shape's    clip back to its original after you perform your smart updating. After saving    the current clip shape, use the path as the "new" clip shape of the picture.    You can set the clip shape of any shape within GX by calling `GXSetShapeClip`    (...). Finally, restore the picture's clip shape back to its original clip    shape. 3. Create a GX offscreen to perform flicker-free updating in a manner similar to using `CopyBits`. This method is based completely on GX. When updating the screen, set the clip shape of the offscreen to represent the area you want to update, and draw the offscreen into the window. For an example, please see the "3 circles - hit testing" sample on the GX SDK, located in the graphics-samples folder. |

#### [May 01 1995]

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
