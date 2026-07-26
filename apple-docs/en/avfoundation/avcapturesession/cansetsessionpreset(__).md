---
title: 'canSetSessionPreset(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/cansetsessionpreset(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/cansetsessionpreset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/cansetsessionpreset%28_%3A%29.json'
content_hash: 'sha256:5bfa8f3c119a964e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# canSetSessionPreset(_:)

<sub>Instance Method</sub>

Determines whether you can configure a capture session with the specified preset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func canSetSessionPreset(_ preset: AVCaptureSession.Preset) -> Bool
```

## Parameters

- `preset` — A preset value to test.

## Return Value

[true](../../swift/true.md) if the capture session supports the preset; otherwise, [false](../../swift/false.md).

## Discussion

Use this method to determine whether the capture session, in its current I/O configuration, supports a particular preset. You can only set a preset that returns [true](../../swift/true.md) as the capture session’s [sessionPreset](sessionpreset.md) property value.

## See Also

### Setting a session preset

- [Preset](preset.md) — Presets that define standard configurations for a capture session.
- [sessionPreset](sessionpreset.md) — A preset value that indicates the quality level or bit rate of the output.
