---
title: itemSeparatorHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-c.class/itemseparatorhandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-c.class/itemseparatorhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-c.class/itemseparatorhandler.json'
content_hash: 'sha256:24f38cb7c0b9256c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-c.class.md)

# itemSeparatorHandler

<sub>Instance Property</sub>

The closure that provides granular control over the list separator appearance of each item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) UICollectionLayoutListItemSeparatorHandler itemSeparatorHandler;
```

## Discussion

The list section treats the configuration that returns from this closure as the final separator configuration for the item at the input index path.

## See Also

### Configuring separators

- [showsSeparators](showsseparators.md) — A Boolean value that determines whether the list shows separators between cells.
- [separatorConfiguration](separatorconfiguration.md) — The section’s preferred configuration for list separators.
- [UIListSeparatorConfiguration](../uilistseparatorconfiguration-c.class.md) — A configuration that controls the list separator appearance in a list section.
- [UICollectionLayoutListItemSeparatorHandler](../uicollectionlayoutlistitemseparatorhandler.md) — A closure that provides granular control over list separator appearance.
