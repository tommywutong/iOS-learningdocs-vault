---
title: 'beginInteractiveMovementForItem(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/begininteractivemovementforitem(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/begininteractivemovementforitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/begininteractivemovementforitem%28at%3A%29.json'
content_hash: 'sha256:1ebb752fc5ef7b83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# beginInteractiveMovementForItem(at:)

<sub>Instance Method</sub>

Initiates the interactive movement of the item at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func beginInteractiveMovementForItem(at indexPath: IndexPath) -> Bool
```

## Parameters

- `indexPath` — The index path of the item you want to move.

## Return Value

[true](../../swift/true.md) if it is possible to move the item or [false](../../swift/false.md) if the item is not allowed to move.

## Discussion

Call this method when you want to begin the interactive movement of an item from its current location to a new location within the same collection view. When using a gesture recognizer to track movements of the item, call this method from your handler method when the gesture recognition process begins. When interactions with the item end, you must call either the [- endInteractiveMovement](<endinteractivemovement().md>) or [- cancelInteractiveMovement](<cancelinteractivemovement().md>) method to inform the collection view of that fact.

When you call this method, the collection view consults its delegate to make sure the item can be moved. If the data source does not support the movement of the item, this method returns [false](../../swift/false.md).

## See Also

### Reordering items interactively

- [- updateInteractiveMovementTargetPosition:](<updateinteractivemovementtargetposition(__).md>) — Updates the position of the item within the collection view’s bounds.
- [- endInteractiveMovement](<endinteractivemovement().md>) — Ends interactive movement tracking and moves the target item to its new location.
- [- cancelInteractiveMovement](<cancelinteractivemovement().md>) — Ends interactive movement tracking and returns the target item to its original location.
