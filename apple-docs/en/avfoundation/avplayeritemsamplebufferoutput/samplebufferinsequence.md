---
title: AVPlayerItemSampleBufferOutput.SampleBufferInSequence
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutput/samplebufferinsequence
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/samplebufferinsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutput/samplebufferinsequence.json'
content_hash: 'sha256:de31ef03f800995e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSampleBufferOutput](../avplayeritemsamplebufferoutput.md)

# AVPlayerItemSampleBufferOutput.SampleBufferInSequence

<sub>Structure</sub>

Holds the information necessary for processing generated sample buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SampleBufferInSequence
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(sampleBuffer:sequenceWasRestarted:)](<samplebufferinsequence/init(samplebuffer_sequencewasrestarted_).md>)

### Instance Properties

- [sampleBuffer](samplebufferinsequence/samplebuffer.md) — Sample buffer containing media data.
- [sequenceWasRestarted](samplebufferinsequence/sequencewasrestarted.md) — Indicates the very first buffer in a new sequence produced by this output. Seeking or changing playback direction will start a new sequence of buffers. If you have any sample buffers queued from the previous sequence, these should be discarded.

## See Also

### Retrieving sample buffers

- [nextAvailableSampleBuffer()](<nextavailablesamplebuffer().md>) — Returns the next sample buffer if it is already available.
- [nextSampleBuffer()](<nextsamplebuffer().md>) — Returns next sample buffer once it becomes available.
