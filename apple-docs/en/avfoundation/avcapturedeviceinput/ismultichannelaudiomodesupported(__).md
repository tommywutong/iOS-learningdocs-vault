---
title: 'isMultichannelAudioModeSupported(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedeviceinput/ismultichannelaudiomodesupported(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/ismultichannelaudiomodesupported(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/ismultichannelaudiomodesupported%28_%3A%29.json'
content_hash: 'sha256:9275d8882015210d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# isMultichannelAudioModeSupported(_:)

<sub>Instance Method</sub>

A Boolean value that indicates whether the input supports the specified multichannel audio mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func isMultichannelAudioModeSupported(_ multichannelAudioMode: AVCaptureMultichannelAudioMode) -> Bool
```

## Parameters

- `multichannelAudioMode` — The multichannel audio mode to test.

## Return Value

[true](../../swift/true.md) if the input supports the mode; otherwise, [false](../../swift/false.md).

## Discussion

You can only set the [multichannelAudioMode](multichannelaudiomode.md) property if the input supports the value.

> [!note] Note
> Multichannel audio modes aren’t supported when used in with [AVCaptureMultiCamSession](../avcapturemulticamsession.md).

## See Also

### Configuring audio properties

- [multichannelAudioMode](multichannelaudiomode.md) — The multichannel audio mode to apply when recording audio.
- [AVCaptureMultichannelAudioMode](../avcapturemultichannelaudiomode.md) — Constants that indicate the modes of multichannel audio.
- [windNoiseRemovalSupported](iswindnoiseremovalsupported.md)
- [windNoiseRemovalEnabled](iswindnoiseremovalenabled.md)
