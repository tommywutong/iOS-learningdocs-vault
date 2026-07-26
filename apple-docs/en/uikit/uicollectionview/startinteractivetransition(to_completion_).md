---
title: 'startInteractiveTransition(to:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/startinteractivetransition(to:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/startinteractivetransition(to:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/startinteractivetransition%28to%3Acompletion%3A%29.json'
content_hash: 'sha256:ee4bc2d9943e0d5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# startInteractiveTransition(to:completion:)

<sub>Instance Method</sub>

Changes the collection view’s current layout using an interactive transition effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func startInteractiveTransition(to layout: UICollectionViewLayout, completion: UICollectionView.LayoutInteractiveTransitionCompletion? = nil) -> UICollectionViewTransitionLayout
```

## Parameters

- `layout` — The new layout object for the collected views. This is the layout that you want the collection view to use after the interactive transition is done.

- `completion` — A completion handler to execute after the transition finishes.

## Return Value

The intermediate transition layout object responsible for managing the interactive transition behavior.

## Discussion

Call this method when you want to change the layout of your collection view using an intermediate transition. When you call this method, the collection view quietly makes the returned transition layout object its current layout object. It is your responsibility to set up a gesture recognizer or other touch-event handling code to track the transition progress. As progress changes, update the [transitionProgress](../uicollectionviewtransitionlayout/transitionprogress.md) property of the transition layout object and invalidate the layout. Invalidating its layout causes the transition layout object to update the position of items based on the new progress value.

When your event-handling code determines that the user has finished the transition to the new layout, call the [- finishInteractiveTransition](<finishinteractivetransition().md>) method. If your code determines that the user has canceled the transition, call the [- cancelInteractiveTransition](<cancelinteractivetransition().md>) method to revert the changes instead. Calling either of these methods removes the transition layout object from the collection view and installs the appropriate target layout object.

This method returns an instance of the [UICollectionViewTransitionLayout](../uicollectionviewtransitionlayout.md) class by default. If you want it to return a custom transition object instead, implement the [- collectionView:transitionLayoutForOldLayout:newLayout:](<../uicollectionviewdelegate/collectionview(__transitionlayoutforoldlayout_newlayout_).md>) method of your collection view delegate and use that method to return your custom object.

## See Also

### Changing the layout

- [collectionViewLayout](collectionviewlayout.md) — The layout used to organize the collected view’s items.
- [- setCollectionViewLayout:animated:](<setcollectionviewlayout(__animated_).md>) — Changes the collection view’s layout and optionally animates the change.
- [- setCollectionViewLayout:animated:completion:](<setcollectionviewlayout(__animated_completion_).md>) — Changes the collection view’s layout and notifies you when the animations complete.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Tells the collection view to finish an interactive transition by installing the intended target layout.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Tells the collection view to cancel an interactive transition and return to its original layout object.
- [LayoutInteractiveTransitionCompletion](layoutinteractivetransitioncompletion.md) — The completion block called at the end of an interactive transition for a collection view.
