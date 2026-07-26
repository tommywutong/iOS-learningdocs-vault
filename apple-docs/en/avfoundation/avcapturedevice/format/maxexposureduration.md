---
title: maxExposureDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/maxexposureduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/maxexposureduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/maxexposureduration.json'
content_hash: 'sha256:1e7a72b2124f9760'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# maxExposureDuration

<sub>Instance Property</sub>

A time value that indicates the maximum supported exposure duration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var maxExposureDuration: CMTime { get }
```

## See Also

### Determining exposure support

- [systemRecommendedExposureBiasRange](systemrecommendedexposurebiasrange.md) — The system’s recommended exposure bias range for this device format.
- [minISO](miniso.md) — A floating-point number that indicates the minimum supported exposure ISO value.
- [maxISO](maxiso.md) — A floating-point number that indicates the maximum supported exposure ISO value.
- [minExposureDuration](minexposureduration.md) — A time value that indicates the minimum supported exposure duration.
