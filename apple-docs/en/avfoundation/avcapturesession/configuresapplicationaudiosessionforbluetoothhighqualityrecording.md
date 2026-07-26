---
title: configuresApplicationAudioSessionForBluetoothHighQualityRecording
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/configuresapplicationaudiosessionforbluetoothhighqualityrecording
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/configuresapplicationaudiosessionforbluetoothhighqualityrecording'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/configuresapplicationaudiosessionforbluetoothhighqualityrecording.json'
content_hash: 'sha256:bc891b80502febfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# configuresApplicationAudioSessionForBluetoothHighQualityRecording

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var configuresApplicationAudioSessionForBluetoothHighQualityRecording: Bool { get set }
```

## Discussion

Use this property to enable using AirPods as a high-quality microphone. Set this value to `true` to tell a capture session to opt-in to high-quality bluetooth recording, which enables a person to select AirPods as the active mic source for capture. This property has no effect when the value of [usesApplicationAudioSession](usesapplicationaudiosession.md) is `false`.

## See Also

### Configuring the app’s audio session

- [usesApplicationAudioSession](usesapplicationaudiosession.md) — A Boolean value that indicates whether the capture session uses the app’s shared audio session.
- [automaticallyConfiguresApplicationAudioSession](automaticallyconfiguresapplicationaudiosession.md) — A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.
- [configuresApplicationAudioSessionToMixWithOthers](configuresapplicationaudiosessiontomixwithothers.md) — A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.
