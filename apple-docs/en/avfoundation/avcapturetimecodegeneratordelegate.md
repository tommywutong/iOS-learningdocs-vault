---
title: AVCaptureTimecodeGeneratorDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegeneratordelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegeneratordelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegeneratordelegate.json'
content_hash: 'sha256:ee5bfc12bae086dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureTimecodeGeneratorDelegate

<sub>Protocol</sub>

A protocol for receiving real-time timecode updates and error notifications from a timecode generator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVCaptureTimecodeGeneratorDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to timecode events

- [- timecodeGenerator:didReceiveUpdate:fromSource:](<avcapturetimecodegeneratordelegate/timecodegenerator(__didreceiveupdate_from_).md>) — Notifies the delegate when new, unaligned timecodes are parsed from the specified source.
- [- timecodeGenerator:didUpdateAvailableSources:](<avcapturetimecodegeneratordelegate/timecodegenerator(__didupdateavailablesources_).md>) — Notifies the delegate when the list of available timecode synchronization sources is updated.
- [- timecodeGenerator:transitionedToSynchronizationStatus:forSource:](<avcapturetimecodegeneratordelegate/timecodegenerator(__transitionedto_for_).md>) — Notifies the delegate when the synchronization status of a timecode source changes.
- [SynchronizationStatus](avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .

## See Also

### Timecode generation

- [AVCaptureTimecodeGenerator](avcapturetimecodegenerator.md) — Generates and synchronizes timecode data from various sources for precise video and audio synchronization.
- [SynchronizationStatus](avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
- [Source](avcapturetimecode/source.md) — Describes a timecode source that a timecode generator can synchronize to.
- [SourceType](avcapturetimecode/sourcetype-swift.enum.md) — Defines possible sources for generating timecode in using a timecode generator.
- [AVCaptureTimecode](avcapturetimecode.md) — This structure represents a timecode, adhering to SMPTE standards, which define precise time information and associated timestamps for video or audio synchronization.
- [AVCaptureTimecodeAdvancedByFrames](<avcapturetimecode/advanced(__by_).md>) — Generates a new timecode by adding a specified number of frames to the given timecode, handling overflow for seconds, minutes, and hours.
- [AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp](<avcapturetimecode/createmetadatasamplebuffer(from_associatedwithpresentationtimestamp_).md>) — Creates a sample buffer containing Timecode Media Description metadata for integration with a video track.
- [AVCaptureTimecodeCreateMetadataSampleBufferForDuration](<avcapturetimecode/createmetadatasamplebuffer(from_forduration_).md>) — Creates a sample buffer containing Timecode Media Description metadata for a specified duration.
