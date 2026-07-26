---
title: 'getCropRectangleRamp(for:startCropRectangle:endCropRectangle:timeRange:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionlayerinstruction/getcroprectangleramp(for:startcroprectangle:endcroprectangle:timerange:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/getcroprectangleramp(for:startcroprectangle:endcroprectangle:timerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/getcroprectangleramp%28for%3Astartcroprectangle%3Aendcroprectangle%3Atimerange%3A%29.json'
content_hash: 'sha256:0c958a57b805eaf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../avvideocompositionlayerinstruction.md)

# getCropRectangleRamp(for:startCropRectangle:endCropRectangle:timeRange:)

<sub>Instance Method</sub>

Obtains the crop rectangle ramp that includes the specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func getCropRectangleRamp(for time: CMTime, startCropRectangle: UnsafeMutablePointer<CGRect>?, endCropRectangle: UnsafeMutablePointer<CGRect>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool
```

## Parameters

- `time` — If a ramp with a time range that contains the specified time has been set, information about the effective ramp for that time is supplied. Otherwise, information about the first ramp that starts after the specified time is supplied.

- `startCropRectangle` — A pointer to a `CGRect` to receive the starting crop rectangle value for the crop rectangle ramp. May be NULL.

- `endCropRectangle` — A pointer to a `CGRect` to receive the ending crop rectangle value for the crop rectangle ramp. This value may be `NULL`.

- `timeRange` — A pointer to a `CMTimeRange` to receive the time range of the crop rectangle ramp. This value may be `NULL`.

## Return Value

[false](../../swift/false.md) will be returned if the specified time is beyond the duration of the last crop rectangle ramp that has been set.

## See Also

### Getting opacity, transform, and cropping ramps

- [cropRectangleRamp(at:)](<croprectangleramp(at_).md>) — Obtains the crop rectangle ramp that includes the specified time.
- [CropRectangleRamp](croprectangleramp.md)
- [opacityRamp(at:)](<opacityramp(at_).md>) — Obtains the opacity ramp that includes a specified time.
- [OpacityRamp](opacityramp.md)
- [- getOpacityRampForTime:startOpacity:endOpacity:timeRange:](<getopacityramp(for_startopacity_endopacity_timerange_).md>) — Obtains the opacity ramp that includes a specified time.
- [transformRamp(at:)](<transformramp(at_).md>) — Obtains the transform ramp that includes a specified time.
- [TransformRamp](transformramp.md)
- [- getTransformRampForTime:startTransform:endTransform:timeRange:](<gettransformramp(for_start_end_timerange_).md>) — Obtains the transform ramp that includes a specified time.
