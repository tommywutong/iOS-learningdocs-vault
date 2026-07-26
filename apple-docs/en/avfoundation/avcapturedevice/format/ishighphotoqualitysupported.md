---
title: isHighPhotoQualitySupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/ishighphotoqualitysupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/ishighphotoqualitysupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/ishighphotoqualitysupported.json'
content_hash: 'sha256:85fef161249c2f05'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isHighPhotoQualitySupported

<sub>Instance Property</sub>

A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isHighPhotoQualitySupported: Bool { get }
```

## Discussion

When this value is [true](../../../swift/true.md), the format produces higher image quality when selecting a quality prioritization of [AVCapturePhotoQualityPrioritizationBalanced](../../avcapturephotooutput/qualityprioritization/balanced.md) or [AVCapturePhotoQualityPrioritizationQuality](../../avcapturephotooutput/qualityprioritization/quality.md) in comparison to [AVCapturePhotoQualityPrioritizationSpeed](../../avcapturephotooutput/qualityprioritization/speed.md).

High-quality formats adhere to the following rules:

- Photo requests that prioritize speed produce the fastest image result, which makes it a good choice for burst captures.
- Photo requests that prioritize speed and quality equally produce higher image quality without dropping frames if a video recording is underway.
- Photo requests that prioritize quality produce high-quality images and may cause frame drops if a video recording is underway. For maximum backward compatibility, photo requests on high photo quality formats only cause video frame drops if your app links against iOS 15 or later.

Formats that don’t support high photo quality produce the same image quality regardless of the current [photoQualityPrioritization](../../avcapturephotosettings/photoqualityprioritization.md) setting.

## See Also

### Determining photo quality

- [supportedMaxPhotoDimensions](supportedmaxphotodimensions.md) — The maximum photo dimension this format supports.
- [highestPhotoQualitySupported](ishighestphotoqualitysupported.md) — A Boolean value that indicates whether this format supports the highest photo quality that the platform delivers.
