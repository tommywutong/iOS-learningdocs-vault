---
title: Metal Best Practices Guide
apple_id: TP40016642
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/NativeScreenScale.html
archived_at: '2026-07-15T03:48:55.192427Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Best Practices Guide](index.md)



## Native Screen Scale (iOS and tvOS)

__Best Practice:__ Render drawables at the exact pixel size of your target display.

The pixel size of your drawables should always match the exact pixel size of their target display. This is critical to avoid rendering to off-screen pixels or incurring an additional sampling stage.

The [UIScreen](https://developer.apple.com/documentation/uikit/uiscreen) class provides two properties that define the native size and scale factor of a physical screen: [nativeBounds](https://developer.apple.com/documentation/uikit/uiscreen/1617810-nativebounds) and [nativeScale](https://developer.apple.com/documentation/uikit/uiscreen/1617825-nativescale). Query the [nativeBounds](https://developer.apple.com/documentation/uikit/uiscreen/1617810-nativebounds) property to determine the native bounding rectangle of the screen, in pixels. Query the [nativeScale](https://developer.apple.com/documentation/uikit/uiscreen/1617825-nativescale) property to determine the native scale factor used to convert points to pixels.

> [!IMPORTANT]
> 

### Use a MetalKit View to Support Native Screen Scale

The [MTKView](https://developer.apple.com/documentation/metalkit/mtkview) class automatically supports native screen scale. By default, the size of the view’s current drawable is always guaranteed to match the size of the view itself.

> [!NOTE]
> 

[Drawables](Drawables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrnknltc)

[Frame Rate (iOS and tvOS)](FrameRate.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrtfvjvomi)
