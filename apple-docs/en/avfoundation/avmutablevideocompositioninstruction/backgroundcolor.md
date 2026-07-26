---
title: backgroundColor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocompositioninstruction/backgroundcolor
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositioninstruction/backgroundcolor.json'
content_hash: 'sha256:faa38572dca944c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionInstruction](../avmutablevideocompositioninstruction.md)

# backgroundColor

<sub>Instance Property</sub>

The background color of the composition.

> [!warning] Deprecated
> Use AVVideoCompositionInstruction.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var backgroundColor: CGColor? { get set }
```

## Discussion

Only solid BGRA colors are supported; patterns and other supported colors are ignored. If the rendered pixel buffer does not have alpha, the alpha value of the background color is ignored.

If the background color is `NULL`, the video compositor uses a default background color of opaque black.

## See Also

### Configuring the instructions

- [layerInstructions](layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks. _(deprecated)_
- [timeRange](timerange.md) — The time range to which the instruction applies. _(deprecated)_
- [enablePostProcessing](enablepostprocessing.md) — A Boolean value that indicates whether the instruction requires post processing. _(deprecated)_
