---
title: layerInstructions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocompositioninstruction/layerinstructions
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/layerinstructions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositioninstruction/layerinstructions.json'
content_hash: 'sha256:b099e61fddab6968'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionInstruction](../avmutablevideocompositioninstruction.md)

# layerInstructions

<sub>Instance Property</sub>

Instructions that specify how to layer and compose video frames from source tracks.

> [!warning] Deprecated
> Use AVVideoCompositionInstruction.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layerInstructions: [AVVideoCompositionLayerInstruction] { get set }
```

## Discussion

Tracks are layered in the composition according to the top-to-bottom order of the `layerInstructions` array; the track with trackID of the first instruction in the array will be layered on top, with the track with the trackID of the second instruction immediately underneath, and so on.

If the property value is `nil`, the output is a fill of the background color.

## See Also

### Configuring the instructions

- [backgroundColor](backgroundcolor.md) — The background color of the composition. _(deprecated)_
- [timeRange](timerange.md) — The time range to which the instruction applies. _(deprecated)_
- [enablePostProcessing](enablepostprocessing.md) — A Boolean value that indicates whether the instruction requires post processing. _(deprecated)_
