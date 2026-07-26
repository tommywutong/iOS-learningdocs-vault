---
title: containsTweening
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstructionprotocol/containstweening
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/containstweening'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstructionprotocol/containstweening.json'
content_hash: 'sha256:46ed9ebb7291a881'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstructionProtocol](../avvideocompositioninstructionprotocol.md)

# containsTweening

<sub>Instance Property</sub>

A Boolean value that indicates whether the composition contains tweening.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var containsTweening: Bool { get }
```

## Discussion

A value of [true](../../swift/true.md) indicates that rendering a frame from the same source buffers and the same composition instruction at two different [compositionTime](../avasynchronousvideocompositionrequest/compositiontime.md) values may yield different output frames. A value of [false](../../swift/false.md) indicates that two compositions yield the same frame.
