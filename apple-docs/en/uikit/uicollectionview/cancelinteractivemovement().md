---
title: cancelInteractiveMovement()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/cancelinteractivemovement()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/cancelinteractivemovement()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/cancelinteractivemovement%28%29.json'
content_hash: 'sha256:9ce96b54df38e89d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# cancelInteractiveMovement()

<sub>Instance Method</sub>

Ends interactive movement tracking and returns the target item to its original location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func cancelInteractiveMovement()
```

## Discussion

Call this method to cancel movement tracking and return the item to its original location. For example, when using a gesture recognizer to track interactions, call this method when the gesture is cancelled. Calling this method lets the collection view know to end the tracking process and return the item to its original location.

## See Also

### Reordering items interactively

- [- beginInteractiveMovementForItemAtIndexPath:](<begininteractivemovementforitem(at_).md>) — Initiates the interactive movement of the item at the specified index path.
- [- updateInteractiveMovementTargetPosition:](<updateinteractivemovementtargetposition(__).md>) — Updates the position of the item within the collection view’s bounds.
- [- endInteractiveMovement](<endinteractivemovement().md>) — Ends interactive movement tracking and moves the target item to its new location.
