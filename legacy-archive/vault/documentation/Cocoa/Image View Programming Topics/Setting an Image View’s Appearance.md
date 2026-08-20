---
title: Image View Programming Topics
apple_id: 10000072i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ImageView/Tasks/SettingImageAppearance.html
archived_at: '2026-07-15T07:16:03.016958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Image View Programming Topics](Introduction%20to%20Image%20Views.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20an%20Image%20View%20to%20Specify%20an%20Image.md)

# Setting an Image View’s Appearance

To set the image, use `setImage:`.

To set the frame style, use `setImageFrameStyle:` with one of these arguments:

- `NSImageFrameNone` shows an invisible frame
- `NSImageFramePhoto` shows a thin black outline and a dropped shadow
- `NSImageFrameGrayBezel` shows a gray, concave bezel that makes the image look sunken
- `NSImageFrameGroove` shows a thin groove that looks etched around the image
- `NSImageFrameButton` shows a convex bezel that makes the image stand out in relief, like a button

To choose how the image is scaled within its frame, use `setImageScaling:` with one of these arguments:

- `NSScaleProportionally`. If the image is too large, it shrinks to fit inside the frame. If the image is too small, it expands. The proportions of the image are preserved.
- `NSScaleToFit`. The image shrinks or expands, and its proportions distort, until it exactly fits the frame.
- `NSScaleNone`. The size and proportions of the image don’t change. If the frame is too small to display the whole image, the edges of the image are trimmed off.

To choose how the image is aligned within its frame, use `setImageAlignment:` with one of these arguments:

- `NSImageAlignLeft`
- `NSImageAlignRight`
- `NSImageAlignCenter`
- `NSImageAlignTop`
- `NSImageAlignBottom`
- `NSImageAlignTopLeft`
- `NSImageAlignTopRight`
- `NSImageAlignBottomLeft`
- `NSImageAlignBottomRight`

[Next](Document%20Revision%20History.md)[Previous](Using%20an%20Image%20View%20to%20Specify%20an%20Image.md)

