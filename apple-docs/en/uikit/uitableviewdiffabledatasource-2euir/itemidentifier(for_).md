---
title: 'itemIdentifier(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdiffabledatasource-2euir/itemidentifier(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/itemidentifier(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasource-2euir/itemidentifier%28for%3A%29.json'
content_hash: 'sha256:bf2b6400da8d841e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDiffableDataSource](../uitableviewdiffabledatasource-2euir.md)

# itemIdentifier(for:)

<sub>Instance Method</sub>

Returns an identifier for the item at the specified index path in the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func itemIdentifier(for indexPath: IndexPath) -> ItemIdentifierType?
```

## Parameters

- `indexPath` — The index path of the item in the table view.

## Return Value

The item’s identifier, or `nil` if no item is found at the provided index path.

## Discussion

This method is a constant time operation, O(1), which means you can look up an index path from its corresponding item identifier with no significant overhead.

## See Also

### Identifying items

- [indexPath(for:)](<indexpath(for_).md>) — Returns an index path for the item with the specified identifier in the table view.
