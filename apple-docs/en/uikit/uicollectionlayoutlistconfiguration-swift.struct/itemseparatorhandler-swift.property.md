---
title: itemSeparatorHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.property.json'
content_hash: 'sha256:19fe8059cc60b2d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-swift.struct.md)

# itemSeparatorHandler

<sub>Instance Property</sub>

The closure that provides granular control over the list separator appearance of each item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var itemSeparatorHandler: UICollectionLayoutListConfiguration.ItemSeparatorHandler? { get set }
```

## Discussion

The list section treats the configuration that returns from this closure as the final separator configuration for the item at the input index path.

## See Also

### Configuring separators

- [showsSeparators](showsseparators.md) — A Boolean value that determines whether the list shows separators between cells.
- [separatorConfiguration](separatorconfiguration.md) — The section’s preferred configuration for list separators.
- [UIListSeparatorConfiguration](../uilistseparatorconfiguration-swift.struct.md) — A configuration that controls the list separator appearance in a list section.
- [ItemSeparatorHandler](itemseparatorhandler-swift.typealias.md) — A closure that provides granular control over list separator appearance.
