---
title: seconds
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturetimecode/seconds
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturetimecode/seconds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturetimecode/seconds.json'
content_hash: 'sha256:e11f7868341eb4c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureTimecode](../avcapturetimecode.md)

# seconds

<sub>Instance Property</sub>

Time component representing the current timecode in seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var seconds: UInt8
```

## See Also

### Accessing timecode components

- [frameDuration](frameduration.md) — Frame duration of the timecode. If unknown, the value is `kCMTimeInvalid`.
- [frames](frames.md) — Frame component of the timecode, indicating the frame count within the second.
- [hours](hours.md) — Time component representing the current timecode in hours.
- [minutes](minutes.md) — Time component representing the current timecode in minutes.
- [userBits](userbits.md) — A 32-bit field carrying SMPTE user bits, which are not strictly standardized. User bits are often used for additional metadata such as scene-take information, reel numbers, or dates, but their exact usage is application-dependent.
