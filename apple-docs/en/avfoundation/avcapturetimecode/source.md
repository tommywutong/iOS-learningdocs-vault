---
title: AVCaptureTimecode.Source
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecode/source
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/source'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/source.json'
content_hash: 'sha256:431e8e59335bf515'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecode](../avcapturetimecode.md)

# AVCaptureTimecode.Source

<sub>Class</sub>

Describes a timecode source that a timecode generator can synchronize to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class Source
```

## Overview

`AVCaptureTimecodeSource` provides information about a specific timecode source available for synchronization in `AVCaptureTimecodeGenerator`. It includes metadata such as the source’s name, type, and unique identifier.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting the source

- [displayName](source/displayname.md) — The name of the timecode source.
- [type](source/type.md) — The type of timecode source.
- [uuid](source/uuid.md) — A unique identifier for the timecode source.

## See Also

### Timecode generation

- [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) — Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md) — A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
- [SourceType](sourcetype-swift.enum.md) — Defines possible sources for generating timecode in using a timecode generator.
- [AVCaptureTimecode](../avcapturetimecode.md) — This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [AVCaptureTimecodeAdvancedByFrames](<advanced(__by_).md>) — Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp](<createmetadatasamplebuffer(from_associatedwithpresentationtimestamp_).md>) — Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [AVCaptureTimecodeCreateMetadataSampleBufferForDuration](<createmetadatasamplebuffer(from_forduration_).md>) — Creates a sample buffer containing Timecode Media Description metadata for a specified duration.
