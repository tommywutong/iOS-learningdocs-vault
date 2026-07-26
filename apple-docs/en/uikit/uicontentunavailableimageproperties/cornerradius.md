---
title: cornerRadius
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailableimageproperties/cornerradius
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableimageproperties/cornerradius'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableimageproperties/cornerradius.json'
content_hash: 'sha256:0b0b9517b6860e07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentUnavailableImageProperties](../uicontentunavailableimageproperties.md)

# cornerRadius

<sub>Instance Property</sub>

The preferred corner radius for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGFloat cornerRadius;
```

## Discussion

The default value is 0. If the image is too small to fit the requested radius, the view adjusts the corner curve and radius to fit.
