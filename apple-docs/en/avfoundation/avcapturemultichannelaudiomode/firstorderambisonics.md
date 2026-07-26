---
title: AVCaptureMultichannelAudioMode.firstOrderAmbisonics
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemultichannelaudiomode/firstorderambisonics
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemultichannelaudiomode/firstorderambisonics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemultichannelaudiomode/firstorderambisonics.json'
content_hash: 'sha256:e2b6784771f8170d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMultichannelAudioMode](../avcapturemultichannelaudiomode.md)

# AVCaptureMultichannelAudioMode.firstOrderAmbisonics

<sub>Case</sub>

An audio mode that indicates the recording uses first-order ambisonics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case firstOrderAmbisonics
```

## Discussion

When recording a QuickTime movie file, the system records a stereo audio track with the first-order ambisonics track for backward playback compatibility.

## See Also

### Modes

- [AVCaptureMultichannelAudioModeNone](none.md) — A mode that indicates there’s no multichannel audio.
- [AVCaptureMultichannelAudioModeStereo](stereo.md) — A mode that indicates the recording uses stereo audio.
