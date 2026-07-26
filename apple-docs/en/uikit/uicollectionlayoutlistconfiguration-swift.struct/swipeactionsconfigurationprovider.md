---
title: UICollectionLayoutListConfiguration.SwipeActionsConfigurationProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/swipeactionsconfigurationprovider
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/swipeactionsconfigurationprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/swipeactionsconfigurationprovider.json'
content_hash: 'sha256:81b90ef9f0c195ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-swift.struct.md)

# UICollectionLayoutListConfiguration.SwipeActionsConfigurationProvider

<sub>Type Alias</sub>

A closure that configures the swipe actions for a cell.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
typealias SwipeActionsConfigurationProvider = (IndexPath) -> UISwipeActionsConfiguration?
```

## See Also

### Customizing swipe actions

- [leadingSwipeActionsConfigurationProvider](leadingswipeactionsconfigurationprovider.md) — The closure that provides the set of actions to display when swiping on the leading edge of the cell.
- [trailingSwipeActionsConfigurationProvider](trailingswipeactionsconfigurationprovider.md) — The closure that provides the set of actions to display when swiping on the trailing edge of the cell.
