---
title: AVCaptureDevice.LensStabilizationStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/lensstabilizationstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/lensstabilizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/lensstabilizationstatus.json'
content_hash: 'sha256:063238a74dd6efd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.LensStabilizationStatus

<sub>Enumeration</sub>

Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
enum LensStabilizationStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Lens stabilization values

- [AVCaptureLensStabilizationStatusUnsupported](lensstabilizationstatus/unsupported.md) — Lens stabilization isn’t available on the device or device configuration that captured this photo.
- [AVCaptureLensStabilizationStatusOff](lensstabilizationstatus/off.md) — Lens stabilization isn’t specified for this photo capture.
- [AVCaptureLensStabilizationStatusActive](lensstabilizationstatus/active.md) — Lens stabilization was active for the full duration of the photo capture.
- [AVCaptureLensStabilizationStatusOutOfRange](lensstabilizationstatus/outofrange.md) — Lens stabilization was enabled for the photo capture, but device motion or capture duration exceeded the stabilization module’s correction limits.
- [AVCaptureLensStabilizationStatusUnavailable](lensstabilizationstatus/unavailable.md) — Lens stabilization was temporarily unavailable during the photo capture.

### Initializers

- [init(rawValue:)](<lensstabilizationstatus/init(rawvalue_).md>)
