---
title: deliveryMode
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptions/deliverymode
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions/deliverymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions/deliverymode.json'
content_hash: 'sha256:00acbf3b25e1d6e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptions](../phimagerequestoptions.md)

# deliveryMode

<sub>Instance Property</sub>

The requested image quality and delivery priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var deliveryMode: PHImageRequestOptionsDeliveryMode { get set }
```

## Discussion

Use this property to tell Photos to provide an image quickly (possibly sacrificing image quality), to provide a high-quality image (possibly sacrificing speed), or to provide both automatically if needed. See [PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md).

## See Also

### Specifying Image Request Options

- [version](version.md) — The version of the image to be requested.
- [PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md) — Options for requesting an image asset with or without adjustments, used by the [version](version.md) property.
- [PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md) — Options for delivering requested image data, used by the [deliveryMode](deliverymode.md) property.
- [resizeMode](resizemode.md) — A mode that specifies how to resize the requested image.
- [PHImageRequestOptionsResizeMode](../phimagerequestoptionsresizemode.md) — Options for how to resize the requested image to fit a target size, used by the [resizeMode](resizemode.md) property.
- [normalizedCropRect](normalizedcroprect.md) — A rectangle for requesting a cropped version of the original image.
