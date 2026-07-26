---
title: UICollectionViewCell.DragState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcell/dragstate
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/dragstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/dragstate.json'
content_hash: 'sha256:7a6defdd536fc5c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# UICollectionViewCell.DragState

<sub>Enumeration</sub>

Constants indicating the current state of the drag operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum DragState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UICollectionViewCellDragStateNone](dragstate/none.md) — The cell isn’t involved in a drag.
- [UICollectionViewCellDragStateLifting](dragstate/lifting.md) — The cell is being animated off of the surface of the collection view.
- [UICollectionViewCellDragStateDragging](dragstate/dragging.md) — The cell is being dragged.

### Initializers

- [init(rawValue:)](<dragstate/init(rawvalue_).md>)

## See Also

### Managing drag state changes

- [- dragStateDidChange:](<dragstatedidchange(__).md>) — Called when the drag state of the cell changes.
