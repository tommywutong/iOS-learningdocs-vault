---
title: AVCaptureDevice.LensStabilizationStatus.unavailable
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/lensstabilizationstatus/unavailable
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/lensstabilizationstatus/unavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/lensstabilizationstatus/unavailable.json'
content_hash: 'sha256:d337120e9ffbee03'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [LensStabilizationStatus](../lensstabilizationstatus.md)

# AVCaptureDevice.LensStabilizationStatus.unavailable

<sub>Case</sub>

Lens stabilization was temporarily unavailable during the photo capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case unavailable
```

## See Also

### Lens stabilization values

- [AVCaptureLensStabilizationStatusUnsupported](unsupported.md) — Lens stabilization isn’t available on the device or device configuration that captured this photo.
- [AVCaptureLensStabilizationStatusOff](off.md) — Lens stabilization isn’t specified for this photo capture.
- [AVCaptureLensStabilizationStatusActive](active.md) — Lens stabilization was active for the full duration of the photo capture.
- [AVCaptureLensStabilizationStatusOutOfRange](outofrange.md) — Lens stabilization was enabled for the photo capture, but device motion or capture duration exceeded the stabilization module’s correction limits.
