---
title: UICollectionLayoutListConfiguration.ItemSeparatorHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/itemseparatorhandler-swift.typealias.json'
content_hash: 'sha256:5823c063861266c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-swift.struct.md)

# UICollectionLayoutListConfiguration.ItemSeparatorHandler

<sub>Type Alias</sub>

A closure that provides granular control over list separator appearance.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
typealias ItemSeparatorHandler = (IndexPath, UIListSeparatorConfiguration) -> UIListSeparatorConfiguration
```

## Parameters

- `indexPath` — The [IndexPath](../../foundation/indexpath.md) of the cell to configure separators for.

- `sectionSeparatorConfiguration` — The list section’s separator configuration for the cell at `indexPath`. This configuration contains the values for separator visibility and insets according to the current state of the item.

## Return Value

The configuration to use for the separators at `indexPath`.

## See Also

### Configuring separators

- [showsSeparators](showsseparators.md) — A Boolean value that determines whether the list shows separators between cells.
- [separatorConfiguration](separatorconfiguration.md) — The section’s preferred configuration for list separators.
- [UIListSeparatorConfiguration](../uilistseparatorconfiguration-swift.struct.md) — A configuration that controls the list separator appearance in a list section.
- [itemSeparatorHandler](itemseparatorhandler-swift.property.md) — The closure that provides granular control over the list separator appearance of each item.
