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
doc_path: '/documentation/uikit/uitableviewcell/dragstatedidchange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/dragstatedidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/dragstatedidchange%28_%3A%29.json'
content_hash: 'sha256:185ffd1436193ed5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# dragStateDidChange(_:)

<sub>Instance Method</sub>

Notifies the cell that its drag status changed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dragStateDidChange(_ dragState: UITableViewCell.DragState)
```

## Parameters

- `dragState` — The new drag state for the cell.

## See Also

### Dragging the row

- [userInteractionEnabledWhileDragging](userinteractionenabledwhiledragging.md) — A Boolean value indicating whether users can interact with a cell while it is being dragged.
- [DragState](dragstate.md) — Constants indicating the current state of a row involved in a drag operation.
