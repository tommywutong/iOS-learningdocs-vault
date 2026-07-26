---
title: 'itemIdentifier(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/itemidentifier(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/itemidentifier(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/itemidentifier%28for%3A%29.json'
content_hash: 'sha256:9635578ac30e1cdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# itemIdentifier(for:)

<sub>Instance Method</sub>

Returns an identifier for the item at the specified index path in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func itemIdentifier(for indexPath: IndexPath) -> ItemIdentifierType?
```

## Parameters

- `indexPath` — The index path of the item in the collection view.

## Return Value

The item’s identifier, or `nil` if no item is found at the provided index path.

## Discussion

This method is a constant time operation, O(1), which means you can look up an item identifier from its corresponding index path with no significant overhead.

## See Also

### Identifying items

- [indexPath(for:)](<indexpath(for_).md>) — Returns an index path for the item with the specified identifier in the collection view.
