---
title: enablePostProcessing
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class/enablepostprocessing
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/enablepostprocessing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class/enablepostprocessing.json'
content_hash: 'sha256:43d5fa8286f72f11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md)

# enablePostProcessing

<sub>Instance Property</sub>

A Boolean value that indicates whether the instruction requires post processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var enablePostProcessing: Bool { get }
```

## Discussion

A value of [false](../../swift/false.md) indicates that no post processing is required for the whole duration of the video composition instruction. The composition process is more efficient if the value is [false](../../swift/false.md).

The value is [true](../../swift/true.md) by default.

## See Also

### Inspecting the instruction

- [backgroundColor](backgroundcolor.md) — The background color of the composition.
- [layerInstructions](layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks.
- [timeRange](timerange.md) — The time range to which the instruction applies.
