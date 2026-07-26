---
title: AVCaptureTimecodeGenerator
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator.json'
content_hash: 'sha256:ef803a05a2c4aa2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureTimecodeGenerator

<sub>Class</sub>

Generates and synchronizes timecode data from various sources for precise video and audio synchronization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureTimecodeGenerator
```

## Overview

The [AVCaptureTimecodeGenerator](avcapturetimecodegenerator.md) class supports multiple timecode sources, including frame counting, system clock synchronization, and MIDI timecode input (MTC). Suitable for playback, recording, or other time-sensitive operations where precise timecode metadata is required.

Use the [- startSynchronizationWithTimecodeSource:](<avcapturetimecodegenerator/startsynchronization(source_).md>) method to set up the desired timecode source.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Generating timecode

- [- generateInitialTimecode](<avcapturetimecodegenerator/generateinitialtimecode().md>) — Generates an initial timecode intended to be the first in a sequence.

### Managing sources

- [currentSource](avcapturetimecodegenerator/currentsource.md) — The active timecode source used by [AVCaptureTimecodeGenerator](avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [availableSources](avcapturetimecodegenerator/availablesources.md) — An array of available timecode synchronization sources that can be used by the timecode generator.
- [frameCountSource](avcapturetimecodegenerator/framecountsource.md) — A frame counter timecode source that operates independently of any internal or external synchronization.
- [realTimeClockSource](avcapturetimecodegenerator/realtimeclocksource.md) — A predefined timecode source synchronized to the real-time system clock.
- [- startSynchronizationWithTimecodeSource:](<avcapturetimecodegenerator/startsynchronization(source_).md>) — Synchronizes the generator with the specified timecode source.

### Configuring the generator

- [synchronizationTimeout](avcapturetimecodegenerator/synchronizationtimeout.md) — The maximum time interval allowed for source synchronization attempts before timing out.
- [timecodeAlignmentOffset](avcapturetimecodegenerator/timecodealignmentoffset.md) — The time offset, in seconds, applied to the generated timecode.
- [timecodeFrameDuration](avcapturetimecodegenerator/timecodeframeduration.md) — The frame duration that the generator will use to generate timecodes.
- [- setDelegate:queue:](<avcapturetimecodegenerator/setdelegate(__queue_).md>) — Assigns a delegate to receive real-time timecode updates and specifies a queue for callbacks.

### Handling delegate callbacks

- [delegate](avcapturetimecodegenerator/delegate.md) — The delegate that receives timecode updates from the timecode generator.
- [delegateCallbackQueue](avcapturetimecodegenerator/delegatecallbackqueue.md) — The dispatch queue on which delegate callbacks are invoked.

## See Also

### Timecode generation

- [AVCaptureTimecodeGeneratorDelegate](avcapturetimecodegeneratordelegate.md) — A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [SynchronizationStatus](avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
- [Source](avcapturetimecode/source.md) — Describes a timecode source that a timecode generator can synchronize to.
- [SourceType](avcapturetimecode/sourcetype-swift.enum.md) — Defines possible sources for generating timecode in using a timecode generator.
- [AVCaptureTimecode](avcapturetimecode.md) — This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [AVCaptureTimecodeAdvancedByFrames](<avcapturetimecode/advanced(__by_).md>) — Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp](<avcapturetimecode/createmetadatasamplebuffer(from_associatedwithpresentationtimestamp_).md>) — Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [AVCaptureTimecodeCreateMetadataSampleBufferForDuration](<avcapturetimecode/createmetadatasamplebuffer(from_forduration_).md>) — Creates a sample buffer containing Timecode Media Description metadata for a specified duration.
