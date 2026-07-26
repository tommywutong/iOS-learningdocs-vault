---
title: sequenceWasRestarted
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutput/samplebufferinsequence/sequencewasrestarted
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/samplebufferinsequence/sequencewasrestarted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutput/samplebufferinsequence/sequencewasrestarted.json'
content_hash: 'sha256:58049ac7adf20f91'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerItemSampleBufferOutput](../../avplayeritemsamplebufferoutput.md) · [SampleBufferInSequence](../samplebufferinsequence.md)

# sequenceWasRestarted

<sub>Instance Property</sub>

Indicates the very first buffer in a new sequence produced by this output. Seeking or changing playback direction will start a new sequence of buffers. If you have any sample buffers queued from the previous sequence, these should be discarded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sequenceWasRestarted: Bool
```
