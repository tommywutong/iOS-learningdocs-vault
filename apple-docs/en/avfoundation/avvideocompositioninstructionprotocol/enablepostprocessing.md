---
title: enablePostProcessing
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstructionprotocol/enablepostprocessing
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/enablepostprocessing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstructionprotocol/enablepostprocessing.json'
content_hash: 'sha256:262d99dfd0028196'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstructionProtocol](../avvideocompositioninstructionprotocol.md)

# enablePostProcessing

<sub>Instance Property</sub>

A Boolean value that indicates whether the composition enables post-processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var enablePostProcessing: Bool { get }
```

## Discussion

A value of [false](../../swift/false.md) indicates to skip post-processing for the duration of the instruction.
