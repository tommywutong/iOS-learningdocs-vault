---
title: usesApplicationAudioSession
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/usesapplicationaudiosession
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/usesapplicationaudiosession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/usesapplicationaudiosession.json'
content_hash: 'sha256:33de9cf4b959f2ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# usesApplicationAudioSession

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture session uses the app’s shared audio session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var usesApplicationAudioSession: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md). If you set the value to [false](../../swift/false.md), the capture session uses a private [AVAudioSession](../../avfaudio/avaudiosession.md) instance for audio recording, which may cause interruptions if your app uses its own audio session for playback.

## See Also

### Configuring the app’s audio session

- [automaticallyConfiguresApplicationAudioSession](automaticallyconfiguresapplicationaudiosession.md) — A Boolean value that indicates whether the capture session automatically changes settings in the app’s shared audio session.
- [configuresApplicationAudioSessionToMixWithOthers](configuresapplicationaudiosessiontomixwithothers.md) — A Boolean value that Indicates whether the capture session configures the app’s audio session to mix with others.
- [configuresApplicationAudioSessionForBluetoothHighQualityRecording](configuresapplicationaudiosessionforbluetoothhighqualityrecording.md) — A Boolean value that indicates whether the capture session configures the app’s audio session for bluetooth high-quality recording.
