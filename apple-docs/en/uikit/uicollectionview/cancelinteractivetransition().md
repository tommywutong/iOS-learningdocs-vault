---
title: cancelInteractiveTransition()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/cancelinteractivetransition()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/cancelinteractivetransition()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/cancelinteractivetransition%28%29.json'
content_hash: 'sha256:08fa3071ff6d3659'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# cancelInteractiveTransition()

<sub>Instance Method</sub>

Tells the collection view to cancel an interactive transition and return to its original layout object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func cancelInteractiveTransition()
```

## Discussion

Call this method after a call to the [- startInteractiveTransitionToCollectionViewLayout:completion:](<startinteractivetransition(to_completion_).md>) method and after you determine through a gesture recognizer or other event-handling code that the user wants to revert to the collection view’s original layout. This method removes the intermediate transition layout object from the collection view and reinstalls the original layout object. It then performs any final animations to get the collection view’s items from their current positions to the positions specified by the original layout object.

After calling this method, you can also remove the gesture recognizer or event-handling code you installed to manage the interactive portions of the transition.

## See Also

### Changing the layout

- [collectionViewLayout](collectionviewlayout.md) — The layout used to organize the collected view’s items.
- [- setCollectionViewLayout:animated:](<setcollectionviewlayout(__animated_).md>) — Changes the collection view’s layout and optionally animates the change.
- [- setCollectionViewLayout:animated:completion:](<setcollectionviewlayout(__animated_completion_).md>) — Changes the collection view’s layout and notifies you when the animations complete.
- [- startInteractiveTransitionToCollectionViewLayout:completion:](<startinteractivetransition(to_completion_).md>) — Changes the collection view’s current layout using an interactive transition effect.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Tells the collection view to finish an interactive transition by installing the intended target layout.
- [LayoutInteractiveTransitionCompletion](layoutinteractivetransitioncompletion.md) — The completion block called at the end of an interactive transition for a collection view.
