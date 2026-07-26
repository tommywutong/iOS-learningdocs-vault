---
title: isConstantColorEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/isconstantcolorenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isconstantcolorenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isconstantcolorenabled.json'
content_hash: 'sha256:8f8322ef3b3e9cbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isConstantColorEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to capture the photo with constant color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isConstantColorEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). Set the value to [true](../../swift/true.md) to capture a constant color photo.

> [!important] Important
> Attempting to enable constant color capture when a photo output’s [constantColorEnabled](../avcapturephotooutput/isconstantcolorenabled.md) is [false](../../swift/false.md), results in the system throwing an exception.

## See Also

### Configuring constant color

- [constantColorFallbackPhotoDeliveryEnabled](isconstantcolorfallbackphotodeliveryenabled.md) — A Boolean value that indicates whether to deliver a fallback photo when taking a constant color capture.
