---
title: backgroundColor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class/backgroundcolor
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class/backgroundcolor.json'
content_hash: 'sha256:52f904d4e30bb525'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md)

# backgroundColor

<sub>Instance Property</sub>

The background color of the composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var backgroundColor: CGColor? { get }
```

## Discussion

Only solid BGRA colors are supported; patterns and other supported colors are ignored. If the rendered pixel buffer does not have alpha, the alpha value of the background color is ignored.

If the background color is `NULL`, the video compositor uses a default background color of opaque black.

## See Also

### Inspecting the instruction

- [layerInstructions](layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks.
- [timeRange](timerange.md) — The time range to which the instruction applies.
- [enablePostProcessing](enablepostprocessing.md) — A Boolean value that indicates whether the instruction requires post processing.
