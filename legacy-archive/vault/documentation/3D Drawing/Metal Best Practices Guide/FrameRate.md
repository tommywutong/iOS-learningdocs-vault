---
title: Metal Best Practices Guide
apple_id: TP40016642
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/FrameRate.html
archived_at: '2026-07-15T03:48:48.756475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Best Practices Guide](index.md)



## Frame Rate (iOS and tvOS)

__Best Practice:__ Present your drawables at a consistent and stable frame rate.

Most apps target a frame rate of 60 FPS, equivalent to 16.67 ms per frame. However, apps that are consistently unable to complete a frame’s work within this time should target a lower frame rate to avoid jitter.

> [!IMPORTANT]
> 

### Querying and Adjusting the Frame Rate

The maximum frame rate of iOS and tvOS devices can be queried through the [maximumFramesPerSecond](https://developer.apple.com/reference/uikit/uiscreen/2806814-maximumframespersecond) property. For iOS devices, this value is usually 60 FPS; for tvOS devices, this value can vary based on the hardware capabilities of an attached screen or the user-selected resolution on Apple TV.

Using an [MTKView](https://developer.apple.com/documentation/metalkit/mtkview) object is the recommended way to adjust your app’s frame rate. By default, the view renders at 60 FPS; to target a different frame rate, set the view’s [preferredFramesPerSecond](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648421-preferredframespersecond) property to your desired value.

> [!NOTE]
> 

### Adjust the Drawable Presentation Time

The [presentDrawable:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443029-present) method registers a drawable presentation to occur as soon as possible, which is usually at the next display refresh interval _after_ the drawable has been rendered or written to. If your app can maintain its maximum target frame rate, as set via the [preferredFramesPerSecond](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648421-preferredframespersecond) property, then simply calling the [presentDrawable:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443029-present) method is enough to maintain a consistent and stable frame rate.

If your app targets a lower-factor frame rate, the display refresh rate (e.g. 60 FPS) may fire more frequently than your app’s render loop (e.g. 30 FPS). This means that the [presentDrawable:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443029-present) method could present a drawable earlier than expected if a frame is rendered before the next display refresh interval (e.g. 16.67 ms intervals).

The [presentDrawable:afterMinimumDuration:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/2806849-present) method allows you to specify a minimum display time for each drawable, meaning that drawable presentations occur only _after_ the previous drawable has spent enough time on the display. This lets you synchronize your drawable’s presentation time with your app’s render loop. The relationship between the [preferredFramesPerSecond](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648421-preferredframespersecond) and [presentDrawable:afterMinimumDuration:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/2806849-present) API is shown in Listing 8-1

__Listing 8-1__Presenting drawables after a minimum display time

1. `view.preferredFramesPerSecond = 30;`
2. `/* ... */`
3. `[commandBuffer presentDrawable:view.currentDrawable afterMinimumDuration:1.0/view.preferredFramesPerSecond];`

[Native Screen Scale (iOS and tvOS)](NativeScreenScale.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqobnknltc)

[Load and Store Actions](LoadandStoreActions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrqfvjvomi)
