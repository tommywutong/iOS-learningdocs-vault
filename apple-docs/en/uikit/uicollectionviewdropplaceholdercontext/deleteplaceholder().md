---
title: deletePlaceholder()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropplaceholdercontext/deleteplaceholder()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropplaceholdercontext/deleteplaceholder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropplaceholdercontext/deleteplaceholder%28%29.json'
content_hash: 'sha256:0ee78cc28c94be48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropPlaceholderContext](../uicollectionviewdropplaceholdercontext.md)

# deletePlaceholder()

<sub>Instance Method</sub>

Removes an unneeded placeholder cell altogether from the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func deletePlaceholder() -> Bool
```

## Return Value

[true](../../swift/true.md) if the placeholder cell was removed, or [false](../../swift/false.md) if the cell was no longer in the collection view.

## Discussion

Use this method to remove a placeholder cell without swapping in a new cell. You might call this method if the user chooses to undo the insertion of a cell or if the contents of the collection view changed.
