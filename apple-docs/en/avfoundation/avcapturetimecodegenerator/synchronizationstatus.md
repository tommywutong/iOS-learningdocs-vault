---
title: AVCaptureTimecodeGenerator.SynchronizationStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus.json'
content_hash: 'sha256:7055625b6d398484'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md)

# AVCaptureTimecodeGenerator.SynchronizationStatus

<sub>Enumeration</sub>

Constants defining the synchronization status of a timecode generator .

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum SynchronizationStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Status values

- [AVCaptureTimecodeGeneratorSynchronizationStatusNotRequired](synchronizationstatus/notrequired.md) — The timecode generator does not require active synchronization for a given source.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSourceSelected](synchronizationstatus/sourceselected.md) — A timecode source has been selected, but synchronization has not yet started.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSourceUnavailable](synchronizationstatus/sourceunavailable.md) — The timecode generator has failed to establish a connection with a given source.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSourceUnsupported](synchronizationstatus/sourceunsupported.md) — The timecode generator is receiving data from the source in an unrecognized format.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSynchronized](synchronizationstatus/synchronized.md) — The timecode generator is successfully synchronized to the selected source, maintaining active timing alignment.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSynchronizing](synchronizationstatus/synchronizing.md) — The timecode generator is actively synchronizing to the selected source.
- [AVCaptureTimecodeGeneratorSynchronizationStatusTimedOut](synchronizationstatus/timedout.md) — The synchronization has timed out.
- [AVCaptureTimecodeGeneratorSynchronizationStatusUnknown](synchronizationstatus/unknown.md) — The initial state before a source is selected or during error conditions.

### Initializers

- [init(rawValue:)](<synchronizationstatus/init(rawvalue_).md>)

## See Also

### Timecode generation

- [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) — Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md) — A protocol for receiving real-time timecode updates and error notifications from a timecode generator.
- [Source](../avcapturetimecode/source.md) — Describes a timecode source that a timecode generator can synchronize to.
- [SourceType](../avcapturetimecode/sourcetype-swift.enum.md) — Defines possible sources for generating timecode in using a timecode generator.
- [AVCaptureTimecode](../avcapturetimecode.md) — This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [AVCaptureTimecodeAdvancedByFrames](<../avcapturetimecode/advanced(__by_).md>) — Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp](<../avcapturetimecode/createmetadatasamplebuffer(from_associatedwithpresentationtimestamp_).md>) — Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [AVCaptureTimecodeCreateMetadataSampleBufferForDuration](<../avcapturetimecode/createmetadatasamplebuffer(from_forduration_).md>) — Creates a sample buffer containing Timecode Media Description metadata for a specified duration.
