---
title: FxPlug SDK Overview
apple_id: TP40002180
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/FXPlug_overview/WhatsNewinFxPlug3.1.1/WhatsNewinFxPlug3.1.1.html
archived_at: '2026-07-15T05:18:04.938421Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FxPlug SDK Overview](About%20the%20FxPlug%20SDK.md)


[Next](FxPlug%20Concepts%20and%20API.md)[Previous](About%20the%20FxPlug%20SDK.md)

# What’s New in FxPlug 3.1.1

The FxPlug 3.1.1 SDK includes the following new feature:

- New [FxColorGamutAPI](https://developer.apple.com/documentation/fxplug/fxcolorgamutapi) for wide color gamut workflows in Final Cut Pro and Motion.

What’s New in Motion 5.3 and FCP 10.3:

- Extract the working gamut of a project or library using [FxColorGamutAPI](https://developer.apple.com/documentation/fxplug/fxcolorgamutapi).
- [FxColorGamutAPI](https://developer.apple.com/documentation/fxplug/fxcolorgamutapi) can calculate the matrices for converting between RGB and YCbCr in the current working wide or standard gamut.
- [dynamicPropertiesAtTime:withError:](https://developer.apple.com/documentation/fxplug/fxbaseeffect/1812217-dynamicpropertiesattime) is called appropriately.
- FxPlug documentation explains which properties can be set in -[dynamicPropertiesAtTime:withError:](https://developer.apple.com/documentation/fxplug/fxbaseeffect/1812217-dynamicpropertiesattime) and -[properties](https://developer.apple.com/documentation/fxplug/fxbaseeffect/1812192-properties).
- Improved thread safety of plug-in rendering.
- Plug-in XPC services are automatically restarted on demand.
- Keyframe times added by [FxKeyframeAPI](https://developer.apple.com/documentation/fxplug/fxkeyframeapi) are correct in Final Cut Pro X.
- Keyframes deleted by a plug-in within Final Cut Pro X are removed.
- Faster transfer of keyframes from the host application to the plug-in.
- Keyframes with times < 0 or > duration are correctly written and read.
- [FxUndoAPI](https://developer.apple.com/documentation/fxplug/fxundoapi) works correctly in Final Cut Pro X.
- All plug-in instances are properly deallocated by the host application.
- Plug-ins can access the API manager and API objects in their `-dealloc` methods.
- [FxOnScreenControlAPI_v4](https://developer.apple.com/documentation/fxplug/fxonscreencontrolapi_v4) supports setting the cursor when using onscreen controls.
- More efficient use of -[parameterChanged:](https://developer.apple.com/documentation/fxplug/fxbaseeffect/1812170-parameterchanged) method, which is properly called once per changed parameter.
- Host applications properly render plug-ins that set the `kFxPropertyKey_PixelIndependent` flag or set their pixel transform support to “Full” in the -[properties](https://developer.apple.com/documentation/fxplug/fxbaseeffect/1812192-properties) method.
- Image size returned from `-getOutputWidth:height:` is now consistent with image size in `-renderOutput:`.
- Fixed an issue that could lead to incorrect 8-bit clamping when retrieving a 32-bit per channel image in an 8-bit per channel buffer.

[Next](FxPlug%20Concepts%20and%20API.md)[Previous](About%20the%20FxPlug%20SDK.md)

