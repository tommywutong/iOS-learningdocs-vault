---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/delegate.json'
content_hash: 'sha256:063b9c8779d7b29a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# delegate

<sub>Instance Property</sub>

The object that acts as the delegate of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UITableViewDelegate)? { get set }
```

## Discussion

The delegate must adopt the [UITableViewDelegate](../uitableviewdelegate.md) protocol. The delegate isn’t retained.

## See Also

### Related Documentation

- [dataSource](datasource.md) — The object that acts as the data source of the table view.

### Managing interactions with the table

- [UITableViewDelegate](../uitableviewdelegate.md) — Methods for managing selections, configuring section headers and footers, deleting and reordering cells, and performing other actions in a table view.
