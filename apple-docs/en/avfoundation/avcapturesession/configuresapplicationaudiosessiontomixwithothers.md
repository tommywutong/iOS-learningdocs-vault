---
title: configuresApplicationAudioSessionToMixWithOthers
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/configuresapplicationaudiosessiontomixwithothers
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/configuresapplicationaudiosessiontomixwithothers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/configuresapplicationaudiosessiontomixwithothers.json'
content_hash: 'sha256:4c6ad93d720f8e45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# configuresApplicationAudioSessionToMixWithOthers

<sub>Instance Property</sub>

A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var configuresApplicationAudioSessionToMixWithOthers: Bool { get set }
```

## Discussion

By default, a capture session’s audio session interrupts the audio of other apps. To enable background audio from other apps to continue while capturing video, set this value to [true](../../swift/true.md).

> [!note] Note
> This property value has no effect when the value of [usesApplicationAudioSession](usesapplicationaudiosession.md) is [false](../../swift/false.md). It also has no effect on Live Photo movie complement capture (where music is always mixed).

The default value is [false](../../swift/false.md).

## See Also

### Configuring the app’s audio session

- [usesApplicationAudioSession](usesapplicationaudiosession.md) — A Boolean value that indicates whether the capture session uses the app’s shared audio session.
- [automaticallyConfiguresApplicationAudioSession](automaticallyconfiguresapplicationaudiosession.md) — A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.
- [configuresApplicationAudioSessionForBluetoothHighQualityRecording](configuresapplicationaudiosessionforbluetoothhighqualityrecording.md) — A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.
