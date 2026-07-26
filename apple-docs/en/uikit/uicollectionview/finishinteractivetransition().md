---
title: finishInteractiveTransition()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/finishinteractivetransition()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/finishinteractivetransition()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/finishinteractivetransition%28%29.json'
content_hash: 'sha256:bf670623bdbc5d8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# finishInteractiveTransition()

<sub>Instance Method</sub>

Tells the collection view to finish an interactive transition by installing the intended target layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func finishInteractiveTransition()
```

## Discussion

Call this method after a call to the [- startInteractiveTransitionToCollectionViewLayout:completion:](<startinteractivetransition(to_completion_).md>) method and after you determine through a gesture recognizer or other event-handling code that the user wants to transition to the new layout. This method removes the intermediate transition layout object from the collection view and installs the intended target layout object. It then performs any final animations to get the collection view’s items from their current positions to the positions specified by the newly installed layout object.

After calling this method, you can also remove the gesture recognizer or event-handling code you installed to manage the interactive portions of the transition.

## See Also

### Changing the layout

- [collectionViewLayout](collectionviewlayout.md) — The layout used to organize the collected view’s items.
- [- setCollectionViewLayout:animated:](<setcollectionviewlayout(__animated_).md>) — Changes the collection view’s layout and optionally animates the change.
- [- setCollectionViewLayout:animated:completion:](<setcollectionviewlayout(__animated_completion_).md>) — Changes the collection view’s layout and notifies you when the animations complete.
- [- startInteractiveTransitionToCollectionViewLayout:completion:](<startinteractivetransition(to_completion_).md>) — Changes the collection view’s current layout using an interactive transition effect.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Tells the collection view to cancel an interactive transition and return to its original layout object.
- [LayoutInteractiveTransitionCompletion](layoutinteractivetransitioncompletion.md) — The completion block called at the end of an interactive transition for a collection view.
