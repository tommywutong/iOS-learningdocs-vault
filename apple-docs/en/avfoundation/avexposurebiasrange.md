---
title: AVExposureBiasRange
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexposurebiasrange
source_url: 'https://developer.apple.com/documentation/avfoundation/avexposurebiasrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexposurebiasrange.json'
content_hash: 'sha256:f25172aea6354c35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVExposureBiasRange

<sub>Class</sub>

An object that expresses an inclusive range of supported exposure bias values, in EV units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface AVExposureBiasRange : NSObject
```

## Overview

A [AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md) defines its range using this type.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Inspecting the exposure bias range

- [minExposureBias](avexposurebiasrange/minexposurebias.md) — The minimum exposure bias in EV units that this range supports.
- [maxExposureBias](avexposurebiasrange/maxexposurebias.md) — The maximum exposure bias in EV units that this range supports.
- [containsExposureBias:](avexposurebiasrange/containsexposurebias_.md) — Determines whether the range contains the specified exposure bias.

## See Also

### Determining exposure support

- [systemRecommendedExposureBiasRange](avcapturedeviceformat/systemrecommendedexposurebiasrange.md) — The system’s recommended exposure bias range for this device format.
- [minISO](avcapturedevice/format/miniso.md) — A floating-point number that indicates the minimum supported exposure ISO value.
- [maxISO](avcapturedevice/format/maxiso.md) — A floating-point number that indicates the maximum supported exposure ISO value.
- [minExposureDuration](avcapturedevice/format/minexposureduration.md) — A time value that indicates the minimum supported exposure duration.
- [maxExposureDuration](avcapturedevice/format/maxexposureduration.md) — A time value that indicates the maximum supported exposure duration.
