---
title: 'setTransform(_:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransform(_:at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransform(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositionlayerinstruction/settransform%28_%3Aat%3A%29.json'
content_hash: 'sha256:e9856f0eed20d0b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionLayerInstruction](../avmutablevideocompositionlayerinstruction.md)

# setTransform(_:at:)

<sub>Instance Method</sub>

Sets the transform value at a time within the time range of the instruction.

> [!warning] Deprecated
> Use AVVideoCompositionLayerInstruction.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTransform(_ transform: CGAffineTransform, at time: CMTime)
```

## Parameters

- `transform` — The transform to be applied at `time`.

- `time` — A time value within the time range of the composition instruction.

## Discussion

Sets a fixed transform to apply from the specified time until the next time at which a transform is set. This is the same as setting a flat ramp for that time range. Before the first specified time for which a transform is set, the affine transform is held constant at the value of [CGAffineTransformIdentity](../../coregraphics/cgaffinetransformidentity.md); after the last time for which a transform is set, the affine transform is held constant at that last value.

## See Also

### Managing properties

- [- setOpacity:atTime:](<setopacity(__at_).md>) — Sets the opacity value at a specific time within the time range of the instruction. _(deprecated)_
- [- setOpacityRampFromStartOpacity:toEndOpacity:timeRange:](<setopacityramp(fromstartopacity_toendopacity_timerange_).md>) — Sets an opacity ramp to apply during a specified time range. _(deprecated)_
- [- setTransformRampFromStartTransform:toEndTransform:timeRange:](<settransformramp(fromstart_toend_timerange_).md>) — Sets a transform ramp to apply during a given time range. _(deprecated)_
