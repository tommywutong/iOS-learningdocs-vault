---
title: preferredSymbolConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/preferredsymbolconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/preferredsymbolconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/preferredsymbolconfiguration.json'
content_hash: 'sha256:acb3081629745e4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# preferredSymbolConfiguration

<sub>Instance Property</sub>

The configuration values to use when rendering the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredSymbolConfiguration: UIImage.SymbolConfiguration? { get set }
```

## Discussion

Use this property to configure the point size, text style, weight, or scale of a symbol image. For example, you might configure the image to be the same weight as text in a neighboring label.

## See Also

### Configuring the appearance of symbol images

- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md) — Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
