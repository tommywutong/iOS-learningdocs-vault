---
title: nextSampleBuffer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutput/nextsamplebuffer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/nextsamplebuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutput/nextsamplebuffer%28%29.json'
content_hash: 'sha256:6d597bd3b286f4dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSampleBufferOutput](../avplayeritemsamplebufferoutput.md)

# nextSampleBuffer()

<sub>Instance Method</sub>

Returns next sample buffer once it becomes available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func nextSampleBuffer() async -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?
```

## Discussion

This method will wait indefinitely for the next sample buffer to become available. This method returns nil if the current task is cancelled or if this method is called from a different task.

This method will race with [nextAvailableSampleBuffer()](<nextavailablesamplebuffer().md>) for grabbing the generated sample buffer.

## See Also

### Retrieving sample buffers

- [nextAvailableSampleBuffer()](<nextavailablesamplebuffer().md>) — Returns the next sample buffer if it is already available.
- [SampleBufferInSequence](samplebufferinsequence.md) — Holds the information necessary for processing generated sample buffers.
