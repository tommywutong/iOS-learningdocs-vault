---
title: isConstantColorFallbackPhotoDeliveryEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/isconstantcolorfallbackphotodeliveryenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isconstantcolorfallbackphotodeliveryenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isconstantcolorfallbackphotodeliveryenabled.json'
content_hash: 'sha256:e800ce10234bf0b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isConstantColorFallbackPhotoDeliveryEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to deliver a fallback photo when taking a constant color capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isConstantColorFallbackPhotoDeliveryEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). Set the value to [true](../../swift/true.md) to receive a fallback photo that you can use if the main constant color photo’s confidence level doesn’t meet your requirement.

## See Also

### Configuring constant color

- [constantColorEnabled](isconstantcolorenabled.md) — A Boolean value that indicates whether to capture the photo with constant color.
