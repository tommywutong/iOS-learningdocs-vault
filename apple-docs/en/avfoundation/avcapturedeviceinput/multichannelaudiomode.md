---
title: multichannelAudioMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/multichannelaudiomode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/multichannelaudiomode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/multichannelaudiomode.json'
content_hash: 'sha256:929f27f089b66bd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# multichannelAudioMode

<sub>Instance Property</sub>

The multichannel audio mode to apply when recording audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var multichannelAudioMode: AVCaptureMultichannelAudioMode { get set }
```

## Discussion

This property only takes effect when the system routes audio through the built-in microphone. The system ignores the value when an external microphone is in use.

The default value is [AVCaptureMultichannelAudioModeNone](../avcapturemultichannelaudiomode/none.md), which indicates to use single channel audio recording.

## See Also

### Configuring audio properties

- [- isMultichannelAudioModeSupported:](<ismultichannelaudiomodesupported(__).md>) — A Boolean value that indicates whether the input supports the specified multichannel audio mode.
- [AVCaptureMultichannelAudioMode](../avcapturemultichannelaudiomode.md) — Constants that indicate the modes of multichannel audio.
- [windNoiseRemovalSupported](iswindnoiseremovalsupported.md)
- [windNoiseRemovalEnabled](iswindnoiseremovalenabled.md)
