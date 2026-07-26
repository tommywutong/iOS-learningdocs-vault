---
title: 'setOpacity(_:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setopacity(_:at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setopacity(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setopacity%28_%3Aat%3A%29.json'
content_hash: 'sha256:66e8aaa4b15b2663'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionLayerInstruction](../avmutablevideocompositionlayerinstruction.md)

# setOpacity(_:at:)

<sub>Instance Method</sub>

Sets the opacity value at a specific time within the time range of the instruction.

> [!warning] Deprecated
> Use AVVideoCompositionLayerInstruction.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setOpacity(_ opacity: Float, at time: CMTime)
```

## Parameters

- `opacity` — The opacity to be applied at `time`. The value must be between `0.0` and `1.0`.

- `time` — A time value within the time range of the composition instruction.

## Discussion

Sets a fixed opacity to apply from the specified time until the next time at which an opacity is set; this is the same as setting a flat ramp for that time range. Before the first time for which an opacity is set, the opacity is held constant at `1.0`; after the last specified time, the opacity is held constant at the last value.

## See Also

### Managing properties

- [- setOpacityRampFromStartOpacity:toEndOpacity:timeRange:](<setopacityramp(fromstartopacity_toendopacity_timerange_).md>) — Sets an opacity ramp to apply during a specified time range. _(deprecated)_
- [- setTransform:atTime:](<settransform(__at_).md>) — Sets the transform value at a time within the time range of the instruction. _(deprecated)_
- [- setTransformRampFromStartTransform:toEndTransform:timeRange:](<settransformramp(fromstart_toend_timerange_).md>) — Sets a transform ramp to apply during a given time range. _(deprecated)_
