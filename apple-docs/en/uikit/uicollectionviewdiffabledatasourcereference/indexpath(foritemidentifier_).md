---
title: 'indexPath(forItemIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasourcereference/indexpath(foritemidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/indexpath(foritemidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereference/indexpath%28foritemidentifier%3A%29.json'
content_hash: 'sha256:89d66ea8fd85b6e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReference](../uicollectionviewdiffabledatasourcereference.md)

# indexPath(forItemIdentifier:)

<sub>Instance Method</sub>

Returns an index path for the item with the specified identifier in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexPath(forItemIdentifier identifier: Any) -> IndexPath?
```

## Parameters

- `identifier` — The identifier of the item in the collection view.

## Return Value

The item’s index path, or `nil` if no item is found with the provided item identifier.

## Discussion

This method is a constant time operation, O(1), which means you can look up an index path from its corresponding item identifier with no significant overhead.

## See Also

### Identifying items

- [- itemIdentifierForIndexPath:](<itemidentifier(for_).md>) — Returns an identifier for the item at the specified index path in the collection view.
