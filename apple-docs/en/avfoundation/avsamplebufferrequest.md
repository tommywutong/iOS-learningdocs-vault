---
title: AVSampleBufferRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest.json'
content_hash: 'sha256:08ec691e78a72093'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferRequest

<sub>Class</sub>

An object that describes a sample buffer creation request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVSampleBufferRequest
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a request

- [- initWithStartCursor:](<avsamplebufferrequest/init(start_).md>) — Creates a newly allocated sample buffer request with the specified sample cursor.

### Configuring sample buffer request parameters

- [direction](avsamplebufferrequest/direction-swift.property.md) — The buffer sample direction.
- [Direction](avsamplebufferrequest/direction-swift.enum.md) — The modes that describe the buffer request direction.
- [limitCursor](avsamplebufferrequest/limitcursor.md) — The limiting position for sample loading.
- [maxSampleCount](avsamplebufferrequest/maxsamplecount.md) — The maximum number of samples to load.
- [mode](avsamplebufferrequest/mode-swift.property.md) — The sample buffer request mode.
- [Mode](avsamplebufferrequest/mode-swift.enum.md) — The modes in which a sample buffer generator processes a request.
- [overrideTime](avsamplebufferrequest/overridetime.md) — The deadline for sample data and output PTS for the sample buffer.
- [preferredMinSampleCount](avsamplebufferrequest/preferredminsamplecount.md) — The preferred minimum number of samples to load.
- [startCursor](avsamplebufferrequest/startcursor.md) — The starting cursor position.

### Initializers

- [init(startCursor:)](<avsamplebufferrequest/init(startcursor_).md>)

## See Also

### Sample buffer generation

- [Playing custom audio with your own player](../avfaudio/playing-custom-audio-with-your-own-player.md) — Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [AVSampleBufferGenerator](avsamplebuffergenerator.md) — An object that creates sample buffers.
- [AVSampleBufferGeneratorBatch](avsamplebuffergeneratorbatch.md) — An object that generates sample buffers in a batch.
