---
title: AVSampleBufferRequest.Direction
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrequest/direction-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum.json'
content_hash: 'sha256:445a3f4711fc6a96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRequest](../avsamplebufferrequest.md)

# AVSampleBufferRequest.Direction

<sub>Enumeration</sub>

The modes that describe the buffer request direction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Direction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Buffer direction

- [AVSampleBufferRequestDirectionForward](direction-swift.enum/forward.md) — The number of following samples may be zero or greater.
- [AVSampleBufferRequestDirectionNone](direction-swift.enum/none.md) — A single sample will be loaded.
- [AVSampleBufferRequestDirectionReverse](direction-swift.enum/reverse.md) — The number of previous samples may be zero or greater.

### Initializers

- [init(rawValue:)](<direction-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring sample buffer request parameters

- [direction](direction-swift.property.md) — The buffer sample direction.
- [limitCursor](limitcursor.md) — The limiting position for sample loading.
- [maxSampleCount](maxsamplecount.md) — The maximum number of samples to load.
- [mode](mode-swift.property.md) — The sample buffer request mode.
- [Mode](mode-swift.enum.md) — The modes in which a sample buffer generator processes a request.
- [overrideTime](overridetime.md) — The deadline for sample data and output PTS for the sample buffer.
- [preferredMinSampleCount](preferredminsamplecount.md) — The preferred minimum number of samples to load.
- [startCursor](startcursor.md) — The starting cursor position.
