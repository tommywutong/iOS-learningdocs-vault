---
title: setNeedsCellUpdate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropplaceholdercontext/setneedscellupdate()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropplaceholdercontext/setneedscellupdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropplaceholdercontext/setneedscellupdate%28%29.json'
content_hash: 'sha256:365422c75264086f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropPlaceholderContext](../uicollectionviewdropplaceholdercontext.md)

# setNeedsCellUpdate()

<sub>Instance Method</sub>

Updates the contents of the placeholder cell.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setNeedsCellUpdate()
```

## Discussion

Call this method when you want to update the contents of the placeholder cell. When you call this method, UIKit calls the update handler that you originally passed to the `drop(_:toPlaceholderInsertedAt:withReuseIdentifier:cellUpdateHandler:)` method when creating the cell.

## See Also

### Updating the Placeholder Cell

- [- commitInsertionWithDataSourceUpdates:](<commitinsertion(datasourceupdates_).md>) — Exchanges the placeholder cell for a cell with the final content.
