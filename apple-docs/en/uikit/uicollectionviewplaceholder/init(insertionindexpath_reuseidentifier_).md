---
title: 'init(insertionIndexPath:reuseIdentifier:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewplaceholder/init(insertionindexpath:reuseidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewplaceholder/init(insertionindexpath:reuseidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewplaceholder/init%28insertionindexpath%3Areuseidentifier%3A%29.json'
content_hash: 'sha256:9482e0e8eff8bfbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewPlaceholder](../uicollectionviewplaceholder.md)

# init(insertionIndexPath:reuseIdentifier:)

<sub>Initializer</sub>

Creates a placeholder object with the specified index path and reuse identifier.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(insertionIndexPath: IndexPath, reuseIdentifier: String)
```

## Parameters

- `insertionIndexPath` — The index path at which to insert the placeholder cell.

- `reuseIdentifier` — The reuse identifier to use when dequeueing the cell.

## Return Value

A new placeholder cell object.
