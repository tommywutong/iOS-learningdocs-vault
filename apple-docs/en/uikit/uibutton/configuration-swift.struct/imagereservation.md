---
title: imageReservation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/imagereservation
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/imagereservation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/imagereservation.json'
content_hash: 'sha256:448eecde7f17f3c8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# imageReservation

<sub>Instance Property</sub>

A value that reserves space for the image in the same axis as the edge against which the button places the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var imageReservation: CGFloat { get set }
```

## Discussion

Defaults to `0`. The value reserves space in the axis that corresponds to [imagePlacement](../../uibuttonconfiguration/imageplacement.md). If the image is larger than the reservation value in that axis, the system ignores the reservation value. Otherwise, the system centers the image in the space that the reservation value provides.

If the image is a symbol image, the system scales the reservation value with dynamic type, based on the image configuration.

## See Also

### Configuring images

- [image](image.md) — The foreground image the button displays.
- [imagePadding](imagepadding.md) — The distance between the button’s image and text.
- [imagePlacement](imageplacement.md) — The edge against which the button places the image.
- [imageColorTransformer](imagecolortransformer.md) — A block that transforms the image color when the button state changes.
- [preferredSymbolConfigurationForImage](preferredsymbolconfigurationforimage.md) — A requested configuration object for the button symbol image.
