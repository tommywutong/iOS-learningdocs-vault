---
title: preferredSymbolConfigurationForImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/preferredsymbolconfigurationforimage
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/preferredsymbolconfigurationforimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/preferredsymbolconfigurationforimage.json'
content_hash: 'sha256:d4990125a7116286'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# preferredSymbolConfigurationForImage

<sub>Instance Property</sub>

A requested configuration object for the button symbol image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, readwrite, nullable) UIImageSymbolConfiguration * preferredSymbolConfigurationForImage;
```

## Discussion

A symbol configuration defines details such as the point size, scale, text style, weight, and font of symbol image. The button uses these details to determine which variant of the image to use and how to scale or style the image.

## See Also

### Configuring images

- [image](image.md) — The foreground image the button displays.
- [imagePadding](imagepadding.md) — The distance between the button’s image and text.
- [imagePlacement](imageplacement.md) — The edge against which the button places the image.
- [imageColorTransformer](imagecolortransformer.md) — A block that transforms the image color when the button state changes.
