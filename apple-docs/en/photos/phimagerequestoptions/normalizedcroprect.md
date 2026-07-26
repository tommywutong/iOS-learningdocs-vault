---
title: normalizedCropRect
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptions/normalizedcroprect
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions/normalizedcroprect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions/normalizedcroprect.json'
content_hash: 'sha256:074ff096ece7ef02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptions](../phimagerequestoptions.md)

# normalizedCropRect

<sub>Instance Property</sub>

A rectangle for requesting a cropped version of the original image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var normalizedCropRect: CGRect { get set }
```

## Discussion

To request a cropped image, specify the crop rectangle in a unit coordinate space relative to the image. In this coordinate system, the point `{0.0,0.0}` refers to the upper left corner of the image, and the point `{1.0,1.0}` refers to the opposite corner regardless of the image’s aspect ratio.

This property defaults to [CGRectZero](../../coregraphics/cgrectzero.md), which specifies no cropping.

If you specify a crop rectangle, you must also specify the [PHImageRequestOptionsResizeModeExact](../phimagerequestoptionsresizemode/exact.md) option for the [resizeMode](resizemode.md) property.

## See Also

### Specifying Image Request Options

- [version](version.md) — The version of the image to be requested.
- [PHImageRequestOptionsVersion](../phimagerequestoptionsversion.md) — Options for requesting an image asset with or without adjustments, used by the [version](version.md) property.
- [deliveryMode](deliverymode.md) — The requested image quality and delivery priority.
- [PHImageRequestOptionsDeliveryMode](../phimagerequestoptionsdeliverymode.md) — Options for delivering requested image data, used by the [deliveryMode](deliverymode.md) property.
- [resizeMode](resizemode.md) — A mode that specifies how to resize the requested image.
- [PHImageRequestOptionsResizeMode](../phimagerequestoptionsresizemode.md) — Options for how to resize the requested image to fit a target size, used by the [resizeMode](resizemode.md) property.
