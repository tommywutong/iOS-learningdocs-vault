---
title: 'setCropRectangleRamp(fromStartCropRectangle:toEndCropRectangle:timeRange:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（26.0 起废弃）, iPadOS 7.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.9+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setcroprectangleramp(fromstartcroprectangle:toendcroprectangle:timerange:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setcroprectangleramp(fromstartcroprectangle:toendcroprectangle:timerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setcroprectangleramp%28fromstartcroprectangle%3Atoendcroprectangle%3Atimerange%3A%29.json'
content_hash: 'sha256:8f7b0004f16330b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionLayerInstruction](../avmutablevideocompositionlayerinstruction.md)

# setCropRectangleRamp(fromStartCropRectangle:toEndCropRectangle:timeRange:)

<sub>Instance Method</sub>

Sets a crop rectangle ramp to apply during the specified time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setCropRectangleRamp(fromStartCropRectangle startCropRectangle: CGRect, toEndCropRectangle endCropRectangle: CGRect, timeRange: CMTimeRange)
```

## Parameters

- `startCropRectangle` — The crop rectangle to be applied at the starting time of the `timeRange`.

- `endCropRectangle` — The crop rectangle to be applied at the end time of the timeRange.

- `timeRange` — The time range over which the value of the opacity is interpolated between `startCropRectangle` and `endCropRectangle`.

## Discussion

The origin of the crop rectangle is the top-left corner of the buffer clean aperture rectangle. The crop rectangle is defined in square pixel space, that is, without taking the pixel aspect ratio into account. Crop rectangles extending outside of the clean aperture, are cropped to the clean aperture.

During a crop rectangle ramp, the rectangle is interpolated between the values set at the ramp’s start time and end time. When the starting or ending rectangle is empty, interpolations take into account the origin and size of the empty rectangle.

Before the first specified time for which a crop rectangle is set, the crop rectangle is held constant to [CGRectInfinite](../../coregraphics/cgrectinfinite.md) and after the last time for which a crop rectangle is set, the crop rectangle is held constant at that last value.

## See Also

### Setting crop rectangle values

- [- setCropRectangle:atTime:](<setcroprectangle(__at_).md>) — Sets the crop rectangle  value at a time within the time range of the instruction. _(deprecated)_
