---
title: imageColorTransformer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/imagecolortransformer
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/imagecolortransformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/imagecolortransformer.json'
content_hash: 'sha256:fc59c51eb054f7ce'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# imageColorTransformer

<sub>Instance Property</sub>

A block that transforms the image color when the button state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var imageColorTransformer: UIConfigurationColorTransformer? { get set }
```

## Discussion

Use this property to transform an image to, for example, a monochrome or tinted image.

## See Also

### Configuring images

- [image](image.md) — The foreground image the button displays.
- [imagePadding](imagepadding.md) — The distance between the button’s image and text.
- [imagePlacement](imageplacement.md) — The edge against which the button places the image.
- [imageReservation](imagereservation.md) — A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [preferredSymbolConfigurationForImage](preferredsymbolconfigurationforimage.md) — A requested configuration object for the button symbol image.
