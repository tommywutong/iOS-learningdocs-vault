---
title: AVCaptureTimecodeGenerator.SynchronizationStatus.notRequired
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus/notrequired
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus/notrequired'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus/notrequired.json'
content_hash: 'sha256:2674cc2d0163689d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureTimecodeGenerator](../../avcapturetimecodegenerator.md) · [SynchronizationStatus](../synchronizationstatus.md)

# AVCaptureTimecodeGenerator.SynchronizationStatus.notRequired

<sub>Case</sub>

The timecode generator does not require active synchronization for a given source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case notRequired
```

## See Also

### Status values

- [AVCaptureTimecodeGeneratorSynchronizationStatusSourceSelected](sourceselected.md) — A timecode source has been selected, but synchronization has not yet started.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSourceUnavailable](sourceunavailable.md) — The timecode generator has failed to establish a connection with a given source.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSourceUnsupported](sourceunsupported.md) — The timecode generator is receiving data from the source in an unrecognized format.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSynchronized](synchronized.md) — The timecode generator is successfully synchronized to the selected source, maintaining active timing alignment.
- [AVCaptureTimecodeGeneratorSynchronizationStatusSynchronizing](synchronizing.md) — The timecode generator is actively synchronizing to the selected source.
- [AVCaptureTimecodeGeneratorSynchronizationStatusTimedOut](timedout.md) — The synchronization has timed out.
- [AVCaptureTimecodeGeneratorSynchronizationStatusUnknown](unknown.md) — The initial state before a source is selected or during error conditions.
