---
title: 'advanced(_:by:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturetimecode/advanced(_:by:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/advanced(_:by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/advanced%28_%3Aby%3A%29.json'
content_hash: 'sha256:9a87389a3e6ca7e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecode](../avcapturetimecode.md)

# advanced(_:by:)

<sub>Type Method</sub>

Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
static func advanced(_ timecode: AVCaptureTimecode, by framesToAdd: Int64) -> AVCaptureTimecode
```

## Parameters

- `timecode` — The original [AVCaptureTimecode](../avcapturetimecode.md) to be incremented.

- `framesToAdd` — The number of frames to add to the timecode.

## Return Value

A new [AVCaptureTimecode](../avcapturetimecode.md) struct with the updated time values after adding the specified frames.

## See Also

### Timecode generation

- [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) — Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md) — A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
- [Source](source.md) — Describes a timecode source that a timecode generator can synchronize to.
- [SourceType](sourcetype-swift.enum.md) — Defines possible sources for generating timecode in using a timecode generator.
- [AVCaptureTimecode](../avcapturetimecode.md) — This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp](<createmetadatasamplebuffer(from_associatedwithpresentationtimestamp_).md>) — Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [AVCaptureTimecodeCreateMetadataSampleBufferForDuration](<createmetadatasamplebuffer(from_forduration_).md>) — Creates a sample buffer containing Timecode Media Description metadata for a specified duration.
