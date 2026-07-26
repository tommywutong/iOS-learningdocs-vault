---
title: automaticallyConfiguresApplicationAudioSession
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/automaticallyconfiguresapplicationaudiosession
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/automaticallyconfiguresapplicationaudiosession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/automaticallyconfiguresapplicationaudiosession.json'
content_hash: 'sha256:c7c7a59c4d6d8be3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# automaticallyConfiguresApplicationAudioSession

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var automaticallyConfiguresApplicationAudioSession: Bool { get set }
```

## Discussion

This property only takes effect if the value of the [usesApplicationAudioSession](usesapplicationaudiosession.md) property is [true](../../swift/true.md).

The value of this property defaults to [true](../../swift/true.md), causing the capture session to automatically configure the app’s shared [AVAudioSession](../../avfaudio/avaudiosession.md) instance for optimal recording. For example, if the capture session uses a device’s rear-facing camera, the system sets the audio session’s microphone and polar pattern for optimal recording of sound from that direction. The audio session’s original state isn’t restored after capture finishes.

If you set value to [false](../../swift/false.md), your app is responsible for selecting appropriate audio session settings. Recording may fail if the audio session’s settings are incompatible with the capture session.

## See Also

### Configuring the app’s audio session

- [usesApplicationAudioSession](usesapplicationaudiosession.md) — A Boolean value that indicates whether the capture session uses the app’s shared audio session.
- [configuresApplicationAudioSessionToMixWithOthers](configuresapplicationaudiosessiontomixwithothers.md) — A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.
- [configuresApplicationAudioSessionForBluetoothHighQualityRecording](configuresapplicationaudiosessionforbluetoothhighqualityrecording.md) — A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.
