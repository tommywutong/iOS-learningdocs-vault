---
title: backgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-c.class/backgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-c.class/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-c.class/backgroundcolor.json'
content_hash: 'sha256:6a1ad3c541e6771f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-c.class.md)

# backgroundColor

<sub>Instance Property</sub>

The background color of the list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, strong, nullable) UIColor * backgroundColor;
```

## Discussion

The default vaue is `nil`, which means that the configuration uses the system background color for the specified appearance.

## See Also

### Configuring appearance

- [appearance](appearance.md) — The overall appearance of the list layout.
- [UICollectionLayoutListAppearance](../uicollectionlayoutlistappearance.md) — Constants that describe the appearance of the list.
