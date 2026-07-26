---
title: enablePostProcessing
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocompositioninstruction/enablepostprocessing
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/enablepostprocessing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositioninstruction/enablepostprocessing.json'
content_hash: 'sha256:31d4c683875df390'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionInstruction](../avmutablevideocompositioninstruction.md)

# enablePostProcessing

<sub>Instance Property</sub>

A Boolean value that indicates whether the instruction requires post processing.

> [!warning] Deprecated
> Use AVVideoCompositionInstruction.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var enablePostProcessing: Bool { get set }
```

## Discussion

If no post processing is required for the whole duration of the video composition instruction, set this property to [false](../../swift/false.md) to make the composition process more efficient.

The value is [true](../../swift/true.md) by default.

## See Also

### Configuring the instructions

- [backgroundColor](backgroundcolor.md) — The background color of the composition. _(deprecated)_
- [layerInstructions](layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks. _(deprecated)_
- [timeRange](timerange.md) — The time range to which the instruction applies. _(deprecated)_
