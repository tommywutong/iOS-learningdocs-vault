---
title: layerInstructions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class/layerinstructions
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/layerinstructions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class/layerinstructions.json'
content_hash: 'sha256:eec2c3ebc7a65ae6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md)

# layerInstructions

<sub>Instance Property</sub>

Instructions that specify how to layer and compose video frames from source tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layerInstructions: [AVVideoCompositionLayerInstruction] { get }
```

## Discussion

Tracks are layered in the composition according to the top-to-bottom order of the `layerInstructions` array; the track with `trackID` of the first instruction in the array will be layered on top, with the track with the `trackID` of the second instruction immediately underneath, and so on.

If the property value is `nil`, the output is a fill of the background color.

## See Also

### Inspecting the instruction

- [backgroundColor](backgroundcolor.md) — The background color of the composition.
- [timeRange](timerange.md) — The time range to which the instruction applies.
- [enablePostProcessing](enablepostprocessing.md) — A Boolean value that indicates whether the instruction requires post processing.
