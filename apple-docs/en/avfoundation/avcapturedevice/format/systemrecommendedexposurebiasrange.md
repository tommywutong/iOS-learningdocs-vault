---
title: systemRecommendedExposureBiasRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/systemrecommendedexposurebiasrange
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/systemrecommendedexposurebiasrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/systemrecommendedexposurebiasrange.json'
content_hash: 'sha256:34d7d808a19f7531'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# systemRecommendedExposureBiasRange

<sub>Instance Property</sub>

The system’s recommended exposure bias range for this device format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc var systemRecommendedExposureBiasRange: ClosedRange<Float>? { get }
```

## Discussion

Use this value to create a slider in your app’s user interface that controls a device’s exposure bias within a system-recommended range. When a recommendation isn’t available, this property returns `nil`.

> [!note] Note
> The framework uses this value to define the range of an [AVCaptureSystemExposureBiasSlider](../../avcapturesystemexposurebiasslider.md) control.

## See Also

### Determining exposure support

- [minISO](miniso.md) — A floating-point number that indicates the minimum supported exposure ISO value.
- [maxISO](maxiso.md) — A floating-point number that indicates the maximum supported exposure ISO value.
- [minExposureDuration](minexposureduration.md) — A time value that indicates the minimum supported exposure duration.
- [maxExposureDuration](maxexposureduration.md) — A time value that indicates the maximum supported exposure duration.
