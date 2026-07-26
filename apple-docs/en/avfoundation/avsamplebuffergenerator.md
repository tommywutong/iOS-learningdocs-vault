---
title: AVSampleBufferGenerator
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffergenerator
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffergenerator.json'
content_hash: 'sha256:33dc7865beb1bf6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferGenerator

<sub>Class</sub>

An object that creates sample buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVSampleBufferGenerator
```

## Overview

Each request for `CMSampleBuffer` creation is described in an `AVSampleBufferRequest` object. The [CMSampleBuffer](../coremedia/cmsamplebuffer.md) opaque objects are returned synchronously. If requested, sample data may be loaded asynchronously (depending on file format support).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating sample buffer generators

- [- initWithAsset:timebase:](<avsamplebuffergenerator/init(asset_timebase_).md>) — Creates a new sample buffer generator.

### Creating a sample buffer

- [- createSampleBufferForRequest:error:](<avsamplebuffergenerator/makesamplebuffer(for_).md>) — Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [- makeBatch](<avsamplebuffergenerator/makebatch().md>) — Creates a batch object to handle generating multiple sample buffers.
- [- createSampleBufferForRequest:addingToBatch:error:](<avsamplebuffergenerator/makesamplebuffer(for_addto_).md>) — Creates a sample buffer and attempts to defer I/O for its data.
- [- createSampleBufferForRequest:](<avsamplebuffergenerator/createsamplebuffer(for_).md>) — Creates a new sample buffer reference for the specified buffer request. _(deprecated)_

### Retrieving sample buffer data

- [+ notifyOfDataReadyForSampleBuffer:completionHandler:](<avsamplebuffergenerator/notifyofdataready(for_completionhandler_).md>) — Notifies the sample buffer generator when data is ready for the sample buffer reference or an error has occurred.

## See Also

### Sample buffer generation

- [Playing custom audio with your own player](../avfaudio/playing-custom-audio-with-your-own-player.md) — Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [AVSampleBufferRequest](avsamplebufferrequest.md) — An object that describes a sample buffer creation request.
- [AVSampleBufferGeneratorBatch](avsamplebuffergeneratorbatch.md) — An object that generates sample buffers in a batch.
