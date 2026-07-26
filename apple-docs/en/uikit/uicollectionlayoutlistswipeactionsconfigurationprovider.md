---
title: UICollectionLayoutListSwipeActionsConfigurationProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistswipeactionsconfigurationprovider
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistswipeactionsconfigurationprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistswipeactionsconfigurationprovider.json'
content_hash: 'sha256:4c3da4fff8ae61fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionLayoutListSwipeActionsConfigurationProvider

<sub>Type Alias</sub>

A closure that configures the swipe actions for a cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef UISwipeActionsConfiguration *(^)(NSIndexPath *) UICollectionLayoutListSwipeActionsConfigurationProvider;
```

## See Also

### Customizing swipe actions

- [leadingSwipeActionsConfigurationProvider](uicollectionlayoutlistconfiguration-c.class/leadingswipeactionsconfigurationprovider.md) — The closure that provides the set of actions to display when swiping on the leading edge of the cell.
- [trailingSwipeActionsConfigurationProvider](uicollectionlayoutlistconfiguration-c.class/trailingswipeactionsconfigurationprovider.md) — The closure that provides the set of actions to display when swiping on the trailing edge of the cell.
