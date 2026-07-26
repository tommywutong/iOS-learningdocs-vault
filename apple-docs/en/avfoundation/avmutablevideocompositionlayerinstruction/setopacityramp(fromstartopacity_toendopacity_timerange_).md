---
title: 'setOpacityRamp(fromStartOpacity:toEndOpacity:timeRange:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setopacityramp(fromstartopacity:toendopacity:timerange:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setopacityramp(fromstartopacity:toendopacity:timerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositionlayerinstruction/setopacityramp%28fromstartopacity%3Atoendopacity%3Atimerange%3A%29.json'
content_hash: 'sha256:71c71089accf41a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionLayerInstruction](../avmutablevideocompositionlayerinstruction.md)

# setOpacityRamp(fromStartOpacity:toEndOpacity:timeRange:)

<sub>Instance Method</sub>

Sets an opacity ramp to apply during a specified time range.

> [!warning] Deprecated
> Use AVVideoCompositionLayerInstruction.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setOpacityRamp(fromStartOpacity startOpacity: Float, toEndOpacity endOpacity: Float, timeRange: CMTimeRange)
```

## Parameters

- `startOpacity` — The opacity to be applied at the start time of `timeRange`. The value must be between `0.0` and `1.0`.

- `endOpacity` — The opacity to be applied at the end time of `timeRange`. The value must be between `0.0` and `1.0`.

- `timeRange` — The time range over which the value of the opacity is interpolated between `startOpacity` and `endOpacity`.

## Discussion

During an opacity ramp, opacity is computed using a linear interpolation. Before the first time for which an opacity is set, the opacity is held constant at `1.0`; after the last specified time, the opacity is held constant at the last value.

## See Also

### Managing properties

- [- setOpacity:atTime:](<setopacity(__at_).md>) — Sets the opacity value at a specific time within the time range of the instruction. _(deprecated)_
- [- setTransform:atTime:](<settransform(__at_).md>) — Sets the transform value at a time within the time range of the instruction. _(deprecated)_
- [- setTransformRampFromStartTransform:toEndTransform:timeRange:](<settransformramp(fromstart_toend_timerange_).md>) — Sets a transform ramp to apply during a given time range. _(deprecated)_
