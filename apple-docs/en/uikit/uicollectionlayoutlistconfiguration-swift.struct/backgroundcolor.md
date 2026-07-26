---
title: backgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/backgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/backgroundcolor.json'
content_hash: 'sha256:9c27d33964d96cb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-swift.struct.md)

# backgroundColor

<sub>Instance Property</sub>

The background color of the list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundColor: UIColor? { get set }
```

## Discussion

The default vaue is `nil`, which means that the configuration uses the system background color for the specified appearance.

## See Also

### Configuring appearance

- [appearance](appearance-swift.property.md) — The overall appearance of the list.
- [Appearance](appearance-swift.enum.md) — Constants that describe the appearance of the list.
