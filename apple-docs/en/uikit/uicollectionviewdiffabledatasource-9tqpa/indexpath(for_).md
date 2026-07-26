---
title: 'indexPath(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/indexpath(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/indexpath(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/indexpath%28for%3A%29.json'
content_hash: 'sha256:41b6a0823acc8509'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# indexPath(for:)

<sub>Instance Method</sub>

Returns an index path for the item with the specified identifier in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func indexPath(for itemIdentifier: ItemIdentifierType) -> IndexPath?
```

## Parameters

- `itemIdentifier` — The identifier of the item in the collection view.

## Return Value

The item’s index path, or `nil` if no item is found with the provided item identifier.

## Discussion

This method is a constant time operation, O(1), which means you can look up an index path from its corresponding item identifier with no significant overhead.

## See Also

### Identifying items

- [itemIdentifier(for:)](<itemidentifier(for_).md>) — Returns an identifier for the item at the specified index path in the collection view.
