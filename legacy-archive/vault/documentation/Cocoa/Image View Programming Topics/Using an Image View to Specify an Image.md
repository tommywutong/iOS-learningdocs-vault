---
title: Image View Programming Topics
apple_id: 10000072i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ImageView/Tasks/MakingImageEditable.html
archived_at: '2026-07-15T07:16:02.501013Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Image View Programming Topics](Introduction%20to%20Image%20Views.md)


[Next](Setting%20an%20Image%20View%E2%80%99s%20Appearance.md)[Previous](Introduction%20to%20Image%20Views.md)

# Using an Image View to Specify an Image

You can use an image view as an image well, which lets a user specify an image by dragging an image to it. Just use `setEditable:` with an argument of `YES`. When the user drags an image to the image view, the image view replaces its old image and sends its action message to its target.

If you don’t want to use the image view as an image well, use `setEditable:` with an argument of `NO`.

[Next](Setting%20an%20Image%20View%E2%80%99s%20Appearance.md)[Previous](Introduction%20to%20Image%20Views.md)

