---
title: AVCaptureMultichannelAudioMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemultichannelaudiomode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemultichannelaudiomode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemultichannelaudiomode.json'
content_hash: 'sha256:7568c0cd15db4c23'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureMultichannelAudioMode

<sub>Enumeration</sub>

Constants that indicate the modes of multichannel audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum AVCaptureMultichannelAudioMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Modes

- [AVCaptureMultichannelAudioModeNone](avcapturemultichannelaudiomode/none.md) — A mode that indicates there’s no multichannel audio.
- [AVCaptureMultichannelAudioModeStereo](avcapturemultichannelaudiomode/stereo.md) — A mode that indicates the recording uses stereo audio.
- [AVCaptureMultichannelAudioModeFirstOrderAmbisonics](avcapturemultichannelaudiomode/firstorderambisonics.md) — An audio mode that indicates the recording uses first-order ambisonics.

### Initializers

- [init(rawValue:)](<avcapturemultichannelaudiomode/init(rawvalue_).md>)

## See Also

### Configuring audio properties

- [- isMultichannelAudioModeSupported:](<avcapturedeviceinput/ismultichannelaudiomodesupported(__).md>) — A Boolean value that indicates whether the input supports the specified multichannel audio mode.
- [multichannelAudioMode](avcapturedeviceinput/multichannelaudiomode.md) — The multichannel audio mode to apply when recording audio.
- [windNoiseRemovalSupported](avcapturedeviceinput/iswindnoiseremovalsupported.md)
- [windNoiseRemovalEnabled](avcapturedeviceinput/iswindnoiseremovalenabled.md)
