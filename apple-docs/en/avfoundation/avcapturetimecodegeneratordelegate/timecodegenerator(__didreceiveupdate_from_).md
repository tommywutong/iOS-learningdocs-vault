---
title: 'timecodeGenerator(_:didReceiveUpdate:from:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator(_:didreceiveupdate:from:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator(_:didreceiveupdate:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator%28_%3Adidreceiveupdate%3Afrom%3A%29.json'
content_hash: 'sha256:6eec8d25a975906b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecodeGeneratorDelegate](../avcapturetimecodegeneratordelegate.md)

# timecodeGenerator(_:didReceiveUpdate:from:)

<sub>Instance Method</sub>

Notifies the delegate when new, unaligned timecodes are parsed from the specified source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func timecodeGenerator(_ generator: AVCaptureTimecodeGenerator, didReceiveUpdate timecode: AVCaptureTimecode, from source: AVCaptureTimecode.Source)
```

## Parameters

- `generator` — The timecode generator providing the update.

- `timecode` — The updated timecode data.

- `source` — The source from which the timecode was received.

## See Also

### Responding to timecode events

- [- timecodeGenerator:didUpdateAvailableSources:](<timecodegenerator(__didupdateavailablesources_).md>) — Notifies the delegate when the list of available timecode synchronization sources is updated.
- [- timecodeGenerator:transitionedToSynchronizationStatus:forSource:](<timecodegenerator(__transitionedto_for_).md>) — Notifies the delegate when the synchronization status of a timecode source changes.
- [SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md) — Constants defining the synchronization status of a timecode generator .
