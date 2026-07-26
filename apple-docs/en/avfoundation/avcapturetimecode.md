---
title: AVCaptureTimecode
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode.json'
content_hash: 'sha256:c5df924d433c5057'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureTimecode

<sub>Structure</sub>

This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
struct AVCaptureTimecode
```

## Overview

This structure corresponds to the SMPTE 12M-1 Linear Timecode (LTC) format, widely used for professional video and audio synchronization.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Accessing timecode components

- [frameDuration](avcapturetimecode/frameduration.md) — Frame duration of the timecode. If unknown, the value is `kCMTimeInvalid`.
- [frames](avcapturetimecode/frames.md) — Frame component of the timecode, indicating the frame count within the second.
- [hours](avcapturetimecode/hours.md) — Time component representing the current timecode in hours.
- [minutes](avcapturetimecode/minutes.md) — Time component representing the current timecode in minutes.
- [seconds](avcapturetimecode/seconds.md) — Time component representing the current timecode in seconds.
- [userBits](avcapturetimecode/userbits.md) — A 32-bit field carrying SMPTE user bits, which are not strictly standardized. User bits are often used for additional metadata such as scene-take information, reel numbers, or dates, but their exact usage is application-dependent.

### Working with sources

- [sourceType](avcapturetimecode/sourcetype-swift.property.md) — Source type of the timecode, indicating the emitter, carriage, or transport mechanism.
- [SourceType](avcapturetimecode/sourcetype-swift.enum.md) — Defines possible sources for generating timecode in using a timecode generator.
- [Source](avcapturetimecode/source.md) — Describes a timecode source that a timecode generator can synchronize to.

### Manipulating timecodes

- [AVCaptureTimecodeAdvancedByFrames](<avcapturetimecode/advanced(__by_).md>) — Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.

### Creating metadata sample buffers

- [AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp](<avcapturetimecode/createmetadatasamplebuffer(from_associatedwithpresentationtimestamp_).md>) — Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [AVCaptureTimecodeCreateMetadataSampleBufferForDuration](<avcapturetimecode/createmetadatasamplebuffer(from_forduration_).md>) — Creates a sample buffer containing Timecode Media Description metadata for a specified duration.

### Initializers

- [init()](<avcapturetimecode/init().md>)
- [init(hours:minutes:seconds:frames:userBits:frameDuration:sourceType:)](<avcapturetimecode/init(hours_minutes_seconds_frames_userbits_frameduration_sourcetype_).md>)

## See Also

### Timecode generation

- [AVCaptureTimecodeGenerator](avcapturetimecodegenerator.md) — Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [AVCaptureTimecodeGeneratorDelegate](avcapturetimecodegeneratordelegate.md) — A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [SynchronizationStatus](avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
- [Source](avcapturetimecode/source.md) — Describes a timecode source that a timecode generator can synchronize to.
- [SourceType](avcapturetimecode/sourcetype-swift.enum.md) — Defines possible sources for generating timecode in using a timecode generator.
- [AVCaptureTimecodeAdvancedByFrames](<avcapturetimecode/advanced(__by_).md>) — Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp](<avcapturetimecode/createmetadatasamplebuffer(from_associatedwithpresentationtimestamp_).md>) — Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [AVCaptureTimecodeCreateMetadataSampleBufferForDuration](<avcapturetimecode/createmetadatasamplebuffer(from_forduration_).md>) — Creates a sample buffer containing Timecode Media Description metadata for a specified duration.
