---
title: 'init(insertionIndexPath:reuseIdentifier:rowHeight:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewplaceholder/init(insertionindexpath:reuseidentifier:rowheight:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewplaceholder/init(insertionindexpath:reuseidentifier:rowheight:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewplaceholder/init%28insertionindexpath%3Areuseidentifier%3Arowheight%3A%29.json'
content_hash: 'sha256:a3a68fc98522c689'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewPlaceholder](../uitableviewplaceholder.md)

# init(insertionIndexPath:reuseIdentifier:rowHeight:)

<sub>Initializer</sub>

Creates a placeholder object with the specified index path and cell-related information.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(insertionIndexPath: IndexPath, reuseIdentifier: String, rowHeight: CGFloat)
```

## Parameters

- `insertionIndexPath` — The index path at which to insert the placeholder cell.

- `reuseIdentifier` — The reuse identifier to use when dequeueing the cell. A cell with the specified identifier must be registered with the table prior to inserting the placeholder cell. You can register cells in your storyboard file or programmatically.

- `rowHeight` — The initial height of the cell. Specify [UITableViewAutomaticDimension](../uitableview/automaticdimension.md) if your table uses estimated row heights and the placeholder cell is self-sizing.

## Return Value

A new placeholder cell object.
