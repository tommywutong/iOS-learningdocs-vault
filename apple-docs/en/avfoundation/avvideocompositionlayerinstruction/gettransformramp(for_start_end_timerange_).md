---
title: 'getTransformRamp(for:start:end:timeRange:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionlayerinstruction/gettransformramp(for:start:end:timerange:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/gettransformramp(for:start:end:timerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionlayerinstruction/gettransformramp%28for%3Astart%3Aend%3Atimerange%3A%29.json'
content_hash: 'sha256:9c804410fd0b4451'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionLayerInstruction](../avvideocompositionlayerinstruction.md)

# getTransformRamp(for:start:end:timeRange:)

<sub>Instance Method</sub>

Obtains the transform ramp that includes a specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func getTransformRamp(for time: CMTime, start startTransform: UnsafeMutablePointer<CGAffineTransform>?, end endTransform: UnsafeMutablePointer<CGAffineTransform>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool
```

## Parameters

- `time` — If a ramp with a time range that contains the specified time has been set, information about the effective ramp for that time is supplied. Otherwise, information about the first ramp that starts after the specified time is supplied.

- `startTransform` — A pointer to a float to receive the starting transform value for the transform ramp. This value may be `NULL`.

- `endTransform` — A pointer to a float to receive the ending transform value for the transform ramp. This value may be `NULL`.

- `timeRange` — A pointer to a `CMTimeRange` to receive the time range of the transform ramp. This value may be `NULL`.

## Return Value

[true](../../swift/true.md) if values are returned successfully, otherwise [false](../../swift/false.md). [false](../../swift/false.md) is returned if `time` is beyond the duration of the last transform ramp that has been set.

## See Also

### Getting opacity, transform, and cropping ramps

- [cropRectangleRamp(at:)](<croprectangleramp(at_).md>) — Obtains the crop rectangle ramp that includes the specified time.
- [CropRectangleRamp](croprectangleramp.md)
- [- getCropRectangleRampForTime:startCropRectangle:endCropRectangle:timeRange:](<getcroprectangleramp(for_startcroprectangle_endcroprectangle_timerange_).md>) — Obtains the crop rectangle ramp that includes the specified time.
- [opacityRamp(at:)](<opacityramp(at_).md>) — Obtains the opacity ramp that includes a specified time.
- [OpacityRamp](opacityramp.md)
- [- getOpacityRampForTime:startOpacity:endOpacity:timeRange:](<getopacityramp(for_startopacity_endopacity_timerange_).md>) — Obtains the opacity ramp that includes a specified time.
- [transformRamp(at:)](<transformramp(at_).md>) — Obtains the transform ramp that includes a specified time.
- [TransformRamp](transformramp.md)
