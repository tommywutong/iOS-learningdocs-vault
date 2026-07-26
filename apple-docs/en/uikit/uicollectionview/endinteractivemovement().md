---
title: endInteractiveMovement()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/endinteractivemovement()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/endinteractivemovement()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/endinteractivemovement%28%29.json'
content_hash: 'sha256:48210d0c13c53558'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# endInteractiveMovement()

<sub>Instance Method</sub>

Ends interactive movement tracking and moves the target item to its new location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func endInteractiveMovement()
```

## Discussion

Call this method upon the successful completion of movement tracking for a item. For example, when using a gesture recognizer to track user interactions, call this method upon the successful completion of the gesture. Calling this method lets the collection view know to end tracking and move the item to its new location permanently. The collection view responds by calling the [- collectionView:moveItemAtIndexPath:toIndexPath:](<../uicollectionviewdatasource/collectionview(__moveitemat_to_).md>) method of its data source to ensure that your data structures are updated.

## See Also

### Reordering items interactively

- [- beginInteractiveMovementForItemAtIndexPath:](<begininteractivemovementforitem(at_).md>) — Initiates the interactive movement of the item at the specified index path.
- [- updateInteractiveMovementTargetPosition:](<updateinteractivemovementtargetposition(__).md>) — Updates the position of the item within the collection view’s bounds.
- [- cancelInteractiveMovement](<cancelinteractivemovement().md>) — Ends interactive movement tracking and returns the target item to its original location.
