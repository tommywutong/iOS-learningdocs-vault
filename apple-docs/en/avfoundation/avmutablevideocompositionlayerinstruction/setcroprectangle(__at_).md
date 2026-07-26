---
title: 'setCropRectangle(_:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（26.0 起废弃）, iPadOS 7.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.9+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setcroprectangle(_:at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setcroprectangle(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setcroprectangle%28_%3Aat%3A%29.json'
content_hash: 'sha256:e4dbfcd33b3b3d63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionLayerInstruction](../avmutablevideocompositionlayerinstruction.md)

# setCropRectangle(_:at:)

<sub>Instance Method</sub>

Sets the crop rectangle  value at a time within the time range of the instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setCropRectangle(_ cropRectangle: CGRect, at time: CMTime)
```

## Parameters

- `cropRectangle` — The crop rectangle to be applied at the specified time.

- `time` — A time value within the timeRange of the composition instruction.

## Discussion

The origin of the crop rectangle is the top-left corner of the buffer clean aperture rectangle. The crop rectangle is defined in square pixel space, that is, without taking the pixel aspect ratio into account. Crop rectangles extending outside of the clean aperture, are cropped to the clean aperture.

Sets a fixed crop rectangle to apply from `time` until the next time at which a crop rectangle is set; this is the same as setting a flat ramp for that time range.

Before the first specified time for which a crop rectangle is set, the crop rectangle is held constant to [CGRectInfinite](../../coregraphics/cgrectinfinite.md) and after the last time for which a crop rectangle is set, the crop rectangle is held constant at that last value.

## See Also

### Setting crop rectangle values

- [- setCropRectangleRampFromStartCropRectangle:toEndCropRectangle:timeRange:](<setcroprectangleramp(fromstartcroprectangle_toendcroprectangle_timerange_).md>) — Sets a crop rectangle ramp to apply during the specified time range. _(deprecated)_
