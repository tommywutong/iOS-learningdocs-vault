---
title: separatorConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-c.class/separatorconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-c.class/separatorconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-c.class/separatorconfiguration.json'
content_hash: 'sha256:5932db4c920d7e1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-c.class.md)

# separatorConfiguration

<sub>Instance Property</sub>

The section’s preferred configuration for list separators.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy) UIListSeparatorConfiguration * separatorConfiguration;
```

## Discussion

This configuration only takes effect if [showsSeparators](showsseparators.md) is [true](../../swift/true.md).

For more granular control over list separator appearance, use [itemSeparatorHandler](itemseparatorhandler.md).

## See Also

### Configuring separators

- [showsSeparators](showsseparators.md) — A Boolean value that determines whether the list shows separators between cells.
- [UIListSeparatorConfiguration](../uilistseparatorconfiguration-c.class.md) — A configuration that controls the list separator appearance in a list section.
- [itemSeparatorHandler](itemseparatorhandler.md) — The closure that provides granular control over the list separator appearance of each item.
- [UICollectionLayoutListItemSeparatorHandler](../uicollectionlayoutlistitemseparatorhandler.md) — A closure that provides granular control over list separator appearance.
