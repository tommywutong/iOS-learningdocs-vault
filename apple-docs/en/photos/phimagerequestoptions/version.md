---
title: version
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptions/version
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions/version.json'
content_hash: 'sha256:553fc6631f8e7897'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptions](../phimagerequestoptions.md)

# version

<sub>Instance Property</sub>

The version of the image to be requested.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var version: PHImageRequestOptionsVersion { get set }
```

## Discussion

Use this property to request a version of the image with or without adjustments, or to request high-quality original data (for example, a RAW file) if such is available. See [PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md).

## See Also

### Specifying Image Request Options

- [PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md) — Options for requesting an image asset with or without adjustments, used by the [version](version.md) property.
- [deliveryMode](deliverymode.md) — The requested image quality and delivery priority.
- [PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md) — Options for delivering requested image data, used by the [deliveryMode](deliverymode.md) property.
- [resizeMode](resizemode.md) — A mode that specifies how to resize the requested image.
- [PHImageRequestOptionsResizeMode](../phimagerequestoptionsresizemode.md) — Options for how to resize the requested image to fit a target size, used by the [resizeMode](resizemode.md) property.
- [normalizedCropRect](normalizedcroprect.md) — A rectangle for requesting a cropped version of the original image.
