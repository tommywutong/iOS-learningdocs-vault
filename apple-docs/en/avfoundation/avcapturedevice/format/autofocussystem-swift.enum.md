---
title: AVCaptureDevice.Format.AutoFocusSystem
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/autofocussystem-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/autofocussystem-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/autofocussystem-swift.enum.json'
content_hash: 'sha256:5ebc8104468af7d4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# AVCaptureDevice.Format.AutoFocusSystem

<sub>Enumeration</sub>

An enumeration of auto focus systems.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum AutoFocusSystem
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Systems

- [AVCaptureAutoFocusSystemNone](autofocussystem-swift.enum/none.md) — Autofocus isn’t available.
- [AVCaptureAutoFocusSystemContrastDetection](autofocussystem-swift.enum/contrastdetection.md) — A slower autofocus system based on differences in contrast.
- [AVCaptureAutoFocusSystemPhaseDetection](autofocussystem-swift.enum/phasedetection.md) — A faster autofoscus system based on differences in light phase.

### Initializers

- [init(rawValue:)](<autofocussystem-swift.enum/init(rawvalue_).md>)

## See Also

### Determining the auto focus system

- [autoFocusSystem](autofocussystem-swift.property.md) — The auto focus system the format uses.
