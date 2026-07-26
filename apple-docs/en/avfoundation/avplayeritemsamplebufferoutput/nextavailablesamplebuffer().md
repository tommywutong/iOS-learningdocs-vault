---
title: nextAvailableSampleBuffer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutput/nextavailablesamplebuffer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/nextavailablesamplebuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutput/nextavailablesamplebuffer%28%29.json'
content_hash: 'sha256:3c0571038bdf5fc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSampleBufferOutput](../avplayeritemsamplebufferoutput.md)

# nextAvailableSampleBuffer()

<sub>Instance Method</sub>

Returns the next sample buffer if it is already available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextAvailableSampleBuffer() -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?
```

## Discussion

If no sample buffers are ready, this method will return nil immediately.

This method will race with [nextSampleBuffer()](<nextsamplebuffer().md>) for grabbing the generated sample buffer.

## See Also

### Retrieving sample buffers

- [nextSampleBuffer()](<nextsamplebuffer().md>) — Returns next sample buffer once it becomes available.
- [SampleBufferInSequence](samplebufferinsequence.md) — Holds the information necessary for processing generated sample buffers.
