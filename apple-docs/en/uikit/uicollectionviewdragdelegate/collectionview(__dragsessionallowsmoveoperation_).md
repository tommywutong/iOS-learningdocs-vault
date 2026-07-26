---
title: 'collectionView(_:dragSessionAllowsMoveOperation:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessionallowsmoveoperation:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessionallowsmoveoperation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdragdelegate/collectionview%28_%3Adragsessionallowsmoveoperation%3A%29.json'
content_hash: 'sha256:7461481dc884f0f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDragDelegate](../uicollectionviewdragdelegate.md)

# collectionView(_:dragSessionAllowsMoveOperation:)

<sub>Instance Method</sub>

Returns a Boolean value that determines whether a move operation is allowed for a drag session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, dragSessionAllowsMoveOperation session: any UIDragSession) -> Bool
```

## Parameters

- `collectionView` — The collection view from which the drag operation originated.

- `session` — The drag session that’s active.

## Return Value

[false](../../swift/false.md) to cancel the drag session if move is not allowed; otherwise, [true](../../swift/true.md).

## Discussion

If you don’t implement this method, the default return value is [true](../../swift/true.md).

## See Also

### Controlling the drag session

- [- collectionView:dragSessionIsRestrictedToDraggingApplication:](<collectionview(__dragsessionisrestrictedtodraggingapplication_).md>) — Returns a Boolean value that determines whether the source app and destination app must be the same for a drag session.
