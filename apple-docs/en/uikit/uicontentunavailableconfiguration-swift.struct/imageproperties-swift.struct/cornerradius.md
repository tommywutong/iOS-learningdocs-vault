---
title: cornerRadius
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/cornerradius
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/cornerradius'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/cornerradius.json'
content_hash: 'sha256:3082f37b5bbcb593'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIContentUnavailableConfiguration](../../uicontentunavailableconfiguration-swift.struct.md) · [ImageProperties](../imageproperties-swift.struct.md)

# cornerRadius

<sub>Instance Property</sub>

The preferred corner radius for the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var cornerRadius: CGFloat { get set }
```

## Discussion

The default value is 0. If the image is too small to fit the requested radius, the view adjusts the corner curve and radius to fit.
