---
title: 'timecodeGenerator(_:didUpdateAvailableSources:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator(_:didupdateavailablesources:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator(_:didupdateavailablesources:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator%28_%3Adidupdateavailablesources%3A%29.json'
content_hash: 'sha256:220bb7e5d2bcab95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md)

# timecodeGenerator(_:didUpdateAvailableSources:)

<sub>Instance Method</sub>

Notifies the delegate when the list of available timecode synchronization sources is updated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func timecodeGenerator(_ generator: AVCaptureTimecodeGenerator, didUpdateAvailableSources availableSources: [AVCaptureTimecode.Source])
```

## Parameters

- `generator` — The [AVCaptureTimecodeGenerator](../avcapturetimecodegenerator.md) instance providing the source list update.

- `availableSources` — An array of [Source](../avcapturetimecode/source.md) objects representing the available timecode synchronization sources.

## See Also

### Responding to timecode events

- [- timecodeGenerator:didReceiveUpdate:fromSource:](<timecodegenerator(__didreceiveupdate_from_).md>) — Notifies the delegate when new, unaligned timecodes are parsed from the specified source.
- [- timecodeGenerator:transitionedToSynchronizationStatus:forSource:](<timecodegenerator(__transitionedto_for_).md>) — Notifies the delegate when the synchronization status of a timecode source changes.
- [SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
