---
title: 'createMetadataSampleBuffer(from:forDuration:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturetimecode/createmetadatasamplebuffer(from:forduration:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/createmetadatasamplebuffer(from:forduration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/createmetadatasamplebuffer%28from%3Aforduration%3A%29.json'
content_hash: 'sha256:a4cda20352ba724c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecode](../avcapturetimecode.md)

# createMetadataSampleBuffer(from:forDuration:)

<sub>Type Method</sub>

Creates a sample buffer containing Timecode Media Description metadata for a specified duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
static func createMetadataSampleBuffer(from timecode: AVCaptureTimecode, forDuration duration: CMTime) -> Unmanaged<CMSampleBuffer>?
```

## Parameters

- `timecode` — The [AVCaptureTimecode](../avcapturetimecode.md) instance providing the timecode details for the metadata sample.

- `duration` — The duration that the metadata sample buffer should represent.

## Return Value

A `CMSampleBufferRef` with encoded Timecode Media Description metadata for the given duration, or `nil` if sample buffer creation fails.

## Discussion

Use this function for scenarios where timecode metadata needs to span a custom interval (not just a single frame), such as non-frame-accurate workflows or for describing a segment of media with a consistent timecode.

## See Also

### Timecode generation

- [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) — Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md) — A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
- [Source](source.md) — Describes a timecode source that a timecode generator can synchronize to.
- [SourceType](sourcetype-swift.enum.md) — Defines possible sources for generating timecode in using a timecode generator.
- [AVCaptureTimecode](../avcapturetimecode.md) — This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [AVCaptureTimecodeAdvancedByFrames](<advanced(__by_).md>) — Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp](<createmetadatasamplebuffer(from_associatedwithpresentationtimestamp_).md>) — Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
