---
title: 'createMetadataSampleBuffer(from:associatedWithPresentationTimeStamp:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturetimecode/createmetadatasamplebuffer(from:associatedwithpresentationtimestamp:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/createmetadatasamplebuffer(from:associatedwithpresentationtimestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/createmetadatasamplebuffer%28from%3Aassociatedwithpresentationtimestamp%3A%29.json'
content_hash: 'sha256:ffebe298ec754dd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecode](../avcapturetimecode.md)

# createMetadataSampleBuffer(from:associatedWithPresentationTimeStamp:)

<sub>Type Method</sub>

Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
static func createMetadataSampleBuffer(from timecode: AVCaptureTimecode, associatedWithPresentationTimeStamp presentationTimeStamp: CMTime) -> Unmanaged<CMSampleBuffer>?
```

## Parameters

- `timecode` — The [AVCaptureTimecode](../avcapturetimecode.md) instance providing the timecode details to encode.

- `presentationTimeStamp` — The presentation time stamp that determines the exact moment in the media timeline where the metadata should be applied. It is embedded in the sample timing info (`CMSampleTimingInfo`) and ensures that the packaged metadata synchronizes accurately with the corresponding video frame.

## Return Value

A `CMSampleBufferRef` with the encoded Timecode Media Description metadata for video synchronization, or `nil` if sample buffer creation fails.

## See Also

### Timecode generation

- [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) — Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md) — A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
- [Source](source.md) — Describes a timecode source that a timecode generator can synchronize to.
- [SourceType](sourcetype-swift.enum.md) — Defines possible sources for generating timecode in using a timecode generator.
- [AVCaptureTimecode](../avcapturetimecode.md) — This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [AVCaptureTimecodeAdvancedByFrames](<advanced(__by_).md>) — Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [AVCaptureTimecodeCreateMetadataSampleBufferForDuration](<createmetadatasamplebuffer(from_forduration_).md>) — Creates a sample buffer containing Timecode Media Description metadata for a specified duration.
