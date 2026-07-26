---
title: AVCaptureTimecode.SourceType
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/sourcetype-swift.enum.json'
content_hash: 'sha256:65465e0d7363a2af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecode](../avcapturetimecode.md)

# AVCaptureTimecode.SourceType

<sub>Enumeration</sub>

Defines possible sources for generating timecode in using a timecode generator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum SourceType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Source types

- [AVCaptureTimecodeSourceTypeExternal](sourcetype-swift.enum/external.md) — Synchronizes timecode to an external timecode data stream. Ideal for professional audio and video synchronization with external quarter-frame MIDI or HID timecode hardware.
- [AVCaptureTimecodeSourceTypeFrameCount](sourcetype-swift.enum/framecount.md) — No internal or external source is adopted. Timecodes are zero-based, sequentially generated frame counts.
- [AVCaptureTimecodeSourceTypeRealTimeClock](sourcetype-swift.enum/realtimeclock.md) — Synchronizes timecode to the system clock for real-time applications. Useful for live events or scenarios requiring alignment with the actual time of day.

### Initializers

- [init(rawValue:)](<sourcetype-swift.enum/init(rawvalue_).md>)

## See Also

### Timecode generation

- [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) — Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md) — A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
- [Source](source.md) — Describes a timecode source that a timecode generator can synchronize to.
- [AVCaptureTimecode](../avcapturetimecode.md) — This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [AVCaptureTimecodeAdvancedByFrames](<advanced(__by_).md>) — Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp](<createmetadatasamplebuffer(from_associatedwithpresentationtimestamp_).md>) — Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [AVCaptureTimecodeCreateMetadataSampleBufferForDuration](<createmetadatasamplebuffer(from_forduration_).md>) — Creates a sample buffer containing Timecode Media Description metadata for a specified duration.
