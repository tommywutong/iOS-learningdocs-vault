---
title: 'updateInteractiveMovementTargetPosition(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/updateinteractivemovementtargetposition(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/updateinteractivemovementtargetposition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/updateinteractivemovementtargetposition%28_%3A%29.json'
content_hash: 'sha256:f2af86a0061c546a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# updateInteractiveMovementTargetPosition(_:)

<sub>Instance Method</sub>

Updates the position of the item within the collection view’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateInteractiveMovementTargetPosition(_ targetPosition: CGPoint)
```

## Parameters

- `targetPosition` — The position of the item in the collection view’s coordinate system.

## Discussion

When moving an item interactively, use this method to provide the collection view with the item’s new position. When using a gesture recognizer to track user interactions with the item, call this method each time the gesture recognizer reports a location change. The collection view uses the new point to determine if the item needs to be repositioned and if the current layout needs to be updated.

For each position change, the collection view reports the change to the [- collectionView:targetIndexPathForMoveFromItemAtIndexPath:toProposedIndexPath:](<../uicollectionviewdelegate/collectionview(__targetindexpathformovefromitemat_toproposedindexpath_).md>) method of its delegate

## See Also

### Reordering items interactively

- [- beginInteractiveMovementForItemAtIndexPath:](<begininteractivemovementforitem(at_).md>) — Initiates the interactive movement of the item at the specified index path.
- [- endInteractiveMovement](<endinteractivemovement().md>) — Ends interactive movement tracking and moves the target item to its new location.
- [- cancelInteractiveMovement](<cancelinteractivemovement().md>) — Ends interactive movement tracking and returns the target item to its original location.
