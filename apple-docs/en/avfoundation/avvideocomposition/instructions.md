---
title: instructions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/instructions
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/instructions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/instructions.json'
content_hash: 'sha256:00bb4d0c7ad927c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# instructions

<sub>Instance Property</sub>

The video composition instructions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instructions: [any AVVideoCompositionInstructionProtocol] { get }
```

## Discussion

The array contains instances of [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md). For the first instruction in the array, `timeRange.start` must be less than or equal to the earliest time for which playback or other processing will be attempted (typically `kCMTimeZero`). For subsequent instructions, `timeRange.start` must be equal to the prior instruction’s end time. The end time of the last instruction must be greater than or equal to the latest time for which playback or other processing will be attempted (typically be the duration of the asset with which the instance of `AVVideoComposition` is associated).

## See Also

### Reading instructions

- [AVVideoCompositionInstructionProtocol](../avvideocompositioninstructionprotocol.md) — A protocol that defines the interface for a video composition instruction.
