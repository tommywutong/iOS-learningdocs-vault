---
title: imagePlacement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/imageplacement
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/imageplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/imageplacement.json'
content_hash: 'sha256:901a50823cb6e429'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# imagePlacement

<sub>Instance Property</sub>

The edge against which the button places the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) NSDirectionalRectEdge imagePlacement;
```

## Discussion

Use this property to place the image along the top, leading, trailing, or bottom edge of the button.

## See Also

### Configuring images

- [image](image.md) — The foreground image the button displays.
- [imagePadding](imagepadding.md) — The distance between the button’s image and text.
- [imageColorTransformer](imagecolortransformer.md) — A block that transforms the image color when the button state changes.
- [preferredSymbolConfigurationForImage](preferredsymbolconfigurationforimage.md) — A requested configuration object for the button symbol image.
