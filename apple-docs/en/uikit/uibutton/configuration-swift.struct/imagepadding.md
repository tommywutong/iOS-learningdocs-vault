---
title: imagePadding
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/configuration-swift.struct/imagepadding
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/imagepadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/configuration-swift.struct/imagepadding.json'
content_hash: 'sha256:29464543152edac0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIButton](../../uibutton.md) · [Configuration](../configuration-swift.struct.md)

# imagePadding

<sub>Instance Property</sub>

The distance between the button’s image and text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var imagePadding: CGFloat { get set }
```

## Discussion

Use this property to adjust the distance from the title and subtitle. This doesn’t affect the distance to the button’s edge.

## See Also

### Configuring images

- [image](image.md) — The foreground image the button displays.
- [imagePlacement](imageplacement.md) — The edge against which the button places the image.
- [imageReservation](imagereservation.md) — A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [imageColorTransformer](imagecolortransformer.md) — A block that transforms the image color when the button state changes.
- [preferredSymbolConfigurationForImage](preferredsymbolconfigurationforimage.md) — A requested configuration object for the button symbol image.
