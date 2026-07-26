---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocompositioninstruction/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocompositioninstruction/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocompositioninstruction/timerange.json'
content_hash: 'sha256:0cd8e957a78341f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoCompositionInstruction](../avmutablevideocompositioninstruction.md)

# timeRange

<sub>Instance Property</sub>

The time range to which the instruction applies.

> [!warning] Deprecated
> Use AVVideoCompositionInstruction.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var timeRange: CMTimeRange { get set }
```

## Discussion

If the time range is invalid, the video compositor ignores it.

## See Also

### Configuring the instructions

- [backgroundColor](backgroundcolor.md) — The background color of the composition. _(deprecated)_
- [layerInstructions](layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks. _(deprecated)_
- [enablePostProcessing](enablepostprocessing.md) — A Boolean value that indicates whether the instruction requires post processing. _(deprecated)_
