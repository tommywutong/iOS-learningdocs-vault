---
title: UICollectionLayoutListItemSeparatorHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistitemseparatorhandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistitemseparatorhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistitemseparatorhandler.json'
content_hash: 'sha256:39cff9bfc3ad3ff4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionLayoutListItemSeparatorHandler

<sub>Type Alias</sub>

A closure that provides granular control over list separator appearance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef UIListSeparatorConfiguration *(^)(NSIndexPath *, UIListSeparatorConfiguration *) UICollectionLayoutListItemSeparatorHandler;
```

## Parameters

- `indexPath` — The [NSIndexPath](../foundation/nsindexpath.md) of the cell to configure separators for.

- `sectionSeparatorConfiguration` — The list section’s separator configuration for the cell at `indexPath`. This configuration contains the values for separator visibility and insets according to the current state of the item.

## Return Value

The configuration to use for the separators at `indexPath`.

## See Also

### Configuring separators

- [showsSeparators](uicollectionlayoutlistconfiguration-c.class/showsseparators.md) — A Boolean value that determines whether the list shows separators between cells.
- [separatorConfiguration](uicollectionlayoutlistconfiguration-c.class/separatorconfiguration.md) — The section’s preferred configuration for list separators.
- [UIListSeparatorConfiguration](uilistseparatorconfiguration-c.class.md) — A configuration that controls the list separator appearance in a list section.
- [itemSeparatorHandler](uicollectionlayoutlistconfiguration-c.class/itemseparatorhandler.md) — The closure that provides granular control over the list separator appearance of each item.
