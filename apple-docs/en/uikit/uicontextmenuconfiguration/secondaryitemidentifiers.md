---
title: secondaryItemIdentifiers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuconfiguration/secondaryitemidentifiers
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/secondaryitemidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuconfiguration/secondaryitemidentifiers.json'
content_hash: 'sha256:ae5e3f0159b9a6e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuConfiguration](../uicontextmenuconfiguration.md)

# secondaryItemIdentifiers

<sub>Instance Property</sub>

A set of identifiers corresponding to each item other than the primary item in a multiple-item interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var secondaryItemIdentifiers: Set<AnyHashable> { get set }
```

## Discussion

When the context menu acts on multiple items, you can use this property to include the identifiers of the secondary items in the configuration. You don’t need to set this property when you create a configuration that originates from a multiple-item interaction in a collection view, such as in [- collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:](<../uicollectionviewdelegate/collectionview(__contextmenuconfigurationforitemsat_point_).md>).

## See Also

### Handling multiple-item interactions

- [badgeCount](badgecount.md) — The number of items in a multiple-item interaction.
