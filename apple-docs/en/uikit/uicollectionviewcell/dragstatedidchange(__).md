---
title: 'dragStateDidChange(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewcell/dragstatedidchange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/dragstatedidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/dragstatedidchange%28_%3A%29.json'
content_hash: 'sha256:b5379a29b37e59ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# dragStateDidChange(_:)

<sub>Instance Method</sub>

Called when the drag state of the cell changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dragStateDidChange(_ dragState: UICollectionViewCell.DragState)
```

## Discussion

Subclasses can override this method and use it to change the cell’s appearance during drag and drop operations. For example, you might use this method to hide or disable controls that you do not want to be visible while the cell is being dragged. You can also use this method to alter the disabled appearance of the cell that remains in the collection view at the original location of the drag.

## See Also

### Managing drag state changes

- [DragState](dragstate.md) — Constants indicating the current state of the drag operation.
