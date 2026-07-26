---
title: image
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/image
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/image.json'
content_hash: 'sha256:e4f5c8546100c1bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# image

<sub>Instance Property</sub>

The foreground image the button displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, strong, readwrite, nullable) UIImage * image;
```

## Discussion

A configuration contains one image. To change the image based on button state, use [configurationUpdateHandler](../uibutton/configurationupdatehandler-swift.property.md) or [- updateConfiguration](<../uibutton/updateconfiguration().md>).

## See Also

### Configuring images

- [imagePadding](imagepadding.md) — The distance between the button’s image and text.
- [imagePlacement](imageplacement.md) — The edge against which the button places the image.
- [imageColorTransformer](imagecolortransformer.md) — A block that transforms the image color when the button state changes.
- [preferredSymbolConfigurationForImage](preferredsymbolconfigurationforimage.md) — A requested configuration object for the button symbol image.
