---
title: imageColorTransformer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/imagecolortransformer
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/imagecolortransformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/imagecolortransformer.json'
content_hash: 'sha256:6cb787197c226efb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# imageColorTransformer

<sub>Instance Property</sub>

A block that transforms the image color when the button state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, readwrite, nullable) UIConfigurationColorTransformer imageColorTransformer;
```

## Discussion

Use this property to transform an image to, for example, a monochrome or tinted image.

## See Also

### Configuring images

- [image](image.md) — The foreground image the button displays.
- [imagePadding](imagepadding.md) — The distance between the button’s image and text.
- [imagePlacement](imageplacement.md) — The edge against which the button places the image.
- [preferredSymbolConfigurationForImage](preferredsymbolconfigurationforimage.md) — A requested configuration object for the button symbol image.
