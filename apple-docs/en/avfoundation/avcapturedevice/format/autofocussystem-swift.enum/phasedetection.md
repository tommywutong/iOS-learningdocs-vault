---
title: AVCaptureDevice.Format.AutoFocusSystem.phaseDetection
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/autofocussystem-swift.enum/phasedetection
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/autofocussystem-swift.enum/phasedetection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/autofocussystem-swift.enum/phasedetection.json'
content_hash: 'sha256:70825ed7670bbcd2'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVCaptureDevice](../../../avcapturedevice.md) · [Format](../../format.md) · [AutoFocusSystem](../autofocussystem-swift.enum.md)

# AVCaptureDevice.Format.AutoFocusSystem.phaseDetection

<sub>Case</sub>

A faster autofoscus system based on differences in light phase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case phaseDetection
```

## Discussion

Phase detection has the ability to achieve focus in many cases without a focus scan. Phase detection autofocus is typically less visually intrusive than contrast detection autofocus.

## See Also

### Systems

- [AVCaptureAutoFocusSystemNone](none.md) — Autofocus isn’t available.
- [AVCaptureAutoFocusSystemContrastDetection](contrastdetection.md) — A slower autofocus system based on differences in contrast.
