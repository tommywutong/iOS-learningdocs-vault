---
title: image
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/image
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/image.json'
content_hash: 'sha256:13f8db47eeb89f0d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# image

<sub>Instance Property</sub>

The foreground image the button displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var image: UIImage? { get set }
```

## Discussion

A configuration contains one image. To change the image based on button state, use [configurationUpdateHandler](../configurationupdatehandler-swift.property.md) or [- updateConfiguration](<../updateconfiguration().md>).

## See Also

### Configuring images

- [imagePadding](imagepadding.md) — The distance between the button’s image and text.
- [imagePlacement](imageplacement.md) — The edge against which the button places the image.
- [imageReservation](imagereservation.md) — A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [imageColorTransformer](imagecolortransformer.md) — A block that transforms the image color when the button state changes.
- [preferredSymbolConfigurationForImage](preferredsymbolconfigurationforimage.md) — A requested configuration object for the button symbol image.
