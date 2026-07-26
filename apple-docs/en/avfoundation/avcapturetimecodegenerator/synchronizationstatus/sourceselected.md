---
title: AVCaptureTimecodeGenerator.SynchronizationStatus.sourceSelected
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus/sourceselected
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus/sourceselected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus/sourceselected.json'
content_hash: 'sha256:52d3af67632cb132'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureTimecodeGenerator](../../avcapturetimecodegenerator.md) · [SynchronizationStatus](../synchronizationstatus.md)

# AVCaptureTimecodeGenerator.SynchronizationStatus.sourceSelected

<sub>Case</sub>

A timecode source has been selected, but synchronization has not yet started.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case sourceSelected
```

## See Also

### Status values

- [AVCaptureTimecodeGeneratorSynchronizationStatusNotRequired](notrequired.md) — The timecode generator does not require active synchronization for a given source.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSourceUnavailable](sourceunavailable.md) — The timecode generator has failed to establish a connection with a given source.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSourceUnsupported](sourceunsupported.md) — The timecode generator is receiving data from the source in an unrecognized format.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSynchronized](synchronized.md) — The timecode generator is successfully synchronized to the selected source, maintaining active timing alignment.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSynchronizing](synchronizing.md) — The timecode generator is actively synchronizing to the selected source.
- [AVCaptureTimecodeGeneratorSynchronizationStatusTimedOut](timedout.md) — The synchronization has timed out.
- [AVCaptureTimecodeGeneratorSynchronizationStatusUnknown](unknown.md) — The initial state before a source is selected or during error conditions.
