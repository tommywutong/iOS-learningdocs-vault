---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class/timerange.json'
content_hash: 'sha256:5f0c1d2aaa49e24b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md)

# timeRange

<sub>Instance Property</sub>

The time range to which the instruction applies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var timeRange: CMTimeRange { get }
```

## Discussion

If the time range is invalid, the video compositor will ignore it. See also the requirements of the [timeRange](timerange.md) property in the array of objects implementing the [AVVideoCompositionInstructionProtocol](../avvideocompositioninstructionprotocol.md) protocol as described in the [AVVideoComposition](../avvideocomposition.md) class’s [instructions](../avvideocomposition/instructions.md) property.

## See Also

### Inspecting the instruction

- [backgroundColor](backgroundcolor.md) — The background color of the composition.
- [layerInstructions](layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks.
- [enablePostProcessing](enablepostprocessing.md) — A Boolean value that indicates whether the instruction requires post processing.
