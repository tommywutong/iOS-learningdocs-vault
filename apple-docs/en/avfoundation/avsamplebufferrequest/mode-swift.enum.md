---
title: AVSampleBufferRequest.Mode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrequest/mode-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/mode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest/mode-swift.enum.json'
content_hash: 'sha256:2b36614180a557b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRequest](../avsamplebufferrequest.md)

# AVSampleBufferRequest.Mode

<sub>Enumeration</sub>

The modes in which a sample buffer generator processes a request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Mode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Mode scheduling

- [AVSampleBufferRequestModeImmediate](mode-swift.enum/immediate.md) — A mode that indicates that sample buffer creation requests load data as soon as possible.
- [AVSampleBufferRequestModeScheduled](mode-swift.enum/scheduled.md) — A mode that indicates that sample buffer creation requests load data according to a scheduled deadline.
- [AVSampleBufferRequestModeOpportunistic](mode-swift.enum/opportunistic.md) — A mode that indicates that opportunistic sample buffer creation requests load data as soon as possible.

### Initializers

- [init(rawValue:)](<mode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring sample buffer request parameters

- [direction](direction-swift.property.md) — The buffer sample direction.
- [Direction](direction-swift.enum.md) — The modes that describe the buffer request direction.
- [limitCursor](limitcursor.md) — The limiting position for sample loading.
- [maxSampleCount](maxsamplecount.md) — The maximum number of samples to load.
- [mode](mode-swift.property.md) — The sample buffer request mode.
- [overrideTime](overridetime.md) — The deadline for sample data and output PTS for the sample buffer.
- [preferredMinSampleCount](preferredminsamplecount.md) — The preferred minimum number of samples to load.
- [startCursor](startcursor.md) — The starting cursor position.
