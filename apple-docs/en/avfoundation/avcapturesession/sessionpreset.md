---
title: sessionPreset
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/sessionpreset
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/sessionpreset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/sessionpreset.json'
content_hash: 'sha256:872c4933d9b13913'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# sessionPreset

<sub>Instance Property</sub>

A preset value that indicates the quality level or bit rate of the output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var sessionPreset: AVCaptureSession.Preset { get set }
```

## Discussion

Specify a preset value to configure a capture session’s format and settings. The default preset is [AVCaptureSessionPresetHigh](preset/high.md), which produces high-quality video and audio output, but you can specify any preset value that returns [true](../../swift/true.md) for a call to [- canSetSessionPreset:](<cansetsessionpreset(__).md>).

You can set this value while the session is running.

## See Also

### Setting a session preset

- [Preset](preset.md) — Presets that define standard configurations for a capture session.
- [- canSetSessionPreset:](<cansetsessionpreset(__).md>) — Determines whether you can configure a capture session with the specified preset.
