---
title: AVSampleBufferGeneratorBatch
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffergeneratorbatch
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergeneratorbatch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergeneratorbatch.json'
content_hash: 'sha256:152a196772edcb92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferGeneratorBatch

<sub>Class</sub>

An object that generates sample buffers in a batch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVSampleBufferGeneratorBatch
```

## Overview

The benefit of batching is it aggregates adjacent I/O requests and overlaps them when possible for all sample buffers within the batch.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Preparing a batch

- [- makeDataReadyWithCompletionHandler:](<avsamplebuffergeneratorbatch/makedataready(completionhandler_).md>) — Loads sample data asynchronously for all sample buffers within a batch.

### Canceling a batch

- [- cancel](<avsamplebuffergeneratorbatch/cancel().md>) — Cancels any I/O for this batch.

## See Also

### Sample buffer generation

- [Playing custom audio with your own player](../avfaudio/playing-custom-audio-with-your-own-player.md) — Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [AVSampleBufferRequest](avsamplebufferrequest.md) — An object that describes a sample buffer creation request.
- [AVSampleBufferGenerator](avsamplebuffergenerator.md) — An object that creates sample buffers.
