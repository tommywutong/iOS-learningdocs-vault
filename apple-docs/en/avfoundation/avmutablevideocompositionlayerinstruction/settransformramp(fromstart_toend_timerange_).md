---
title: 'setTransformRamp(fromStart:toEnd:timeRange:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransformramp(fromstart:toend:timerange:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransformramp(fromstart:toend:timerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransformramp%28fromstart%3Atoend%3Atimerange%3A%29.json'
content_hash: 'sha256:9f63524821023034'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionLayerInstruction](../avmutablevideocompositionlayerinstruction.md)

# setTransformRamp(fromStart:toEnd:timeRange:)

<sub>Instance Method</sub>

Sets a transform ramp to apply during a given time range.

> [!warning] Deprecated
> Use AVVideoCompositionLayerInstruction.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTransformRamp(fromStart startTransform: CGAffineTransform, toEnd endTransform: CGAffineTransform, timeRange: CMTimeRange)
```

## Parameters

- `startTransform` — The transform to be applied at the starting time of `timeRange`.

- `endTransform` — The transform to be applied at the end time of `timeRange`.

- `timeRange` — The time range over which the value of the transform is interpolated between `startTransform` and `endTransform`.

## Discussion

During a transform ramp, the affine transform is interpolated between the values set at the ramp’s start time and end time. Before the first specified time for which a transform is set, the affine transform is held constant at the value of [CGAffineTransformIdentity](../../coregraphics/cgaffinetransformidentity.md); after the last time for which a transform is set, the affine transform is held constant at that last value.

## See Also

### Managing properties

- [- setOpacity:atTime:](<setopacity(__at_).md>) — Sets the opacity value at a specific time within the time range of the instruction. _(deprecated)_
- [- setOpacityRampFromStartOpacity:toEndOpacity:timeRange:](<setopacityramp(fromstartopacity_toendopacity_timerange_).md>) — Sets an opacity ramp to apply during a specified time range. _(deprecated)_
- [- setTransform:atTime:](<settransform(__at_).md>) — Sets the transform value at a time within the time range of the instruction. _(deprecated)_
