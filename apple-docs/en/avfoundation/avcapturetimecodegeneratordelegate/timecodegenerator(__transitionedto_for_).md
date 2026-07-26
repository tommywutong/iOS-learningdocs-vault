---
title: 'timecodeGenerator(_:transitionedTo:for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator(_:transitionedto:for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator(_:transitionedto:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator%28_%3Atransitionedto%3Afor%3A%29.json'
content_hash: 'sha256:9f7a60059d4117e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md)

# timecodeGenerator(_:transitionedTo:for:)

<sub>Instance Method</sub>

Notifies the delegate when the synchronization status of a timecode source changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func timecodeGenerator(_ generator: AVCaptureTimecodeGenerator, transitionedTo synchronizationStatus: AVCaptureTimecodeGenerator.SynchronizationStatus, for source: AVCaptureTimecode.Source)
```

## Parameters

- `generator` — The [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) instance providing the status update.

- `synchronizationStatus` — The updated synchronization state.

- `source` — The internal or external source to which the generator synchronizes.

## See Also

### Responding to timecode events

- [- timecodeGenerator:didReceiveUpdate:fromSource:](<timecodegenerator(__didreceiveupdate_from_).md>) — Notifies the delegate when new, unaligned timecodes are parsed from the specified source.
- [- timecodeGenerator:didUpdateAvailableSources:](<timecodegenerator(__didupdateavailablesources_).md>) — Notifies the delegate when the list of available timecode synchronization sources is updated.
- [SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
