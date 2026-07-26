---
title: resizeMode
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptions/resizemode
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions/resizemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions/resizemode.json'
content_hash: 'sha256:cad20f426a7083a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptions](../phimagerequestoptions.md)

# resizeMode

<sub>Instance Property</sub>

A mode that specifies how to resize the requested image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var resizeMode: PHImageRequestOptionsResizeMode { get set }
```

## Discussion

Use this property to choose how to fit the image to the target size you specified when requesting image data. The default value for this property is [PHImageRequestOptionsResizeModeFast](../phimagerequestoptionsresizemode/fast.md).

## See Also

### Specifying Image Request Options

- [version](version.md) — The version of the image to be requested.
- [PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md) — Options for requesting an image asset with or without adjustments, used by the [version](version.md) property.
- [deliveryMode](deliverymode.md) — The requested image quality and delivery priority.
- [PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md) — Options for delivering requested image data, used by the [deliveryMode](deliverymode.md) property.
- [PHImageRequestOptionsResizeMode](../phimagerequestoptionsresizemode.md) — Options for how to resize the requested image to fit a target size, used by the [resizeMode](resizemode.md) property.
- [normalizedCropRect](normalizedcroprect.md) — A rectangle for requesting a cropped version of the original image.
