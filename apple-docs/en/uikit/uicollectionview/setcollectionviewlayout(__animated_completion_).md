---
title: 'setCollectionViewLayout(_:animated:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/setcollectionviewlayout(_:animated:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/setcollectionviewlayout(_:animated:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/setcollectionviewlayout%28_%3Aanimated%3Acompletion%3A%29.json'
content_hash: 'sha256:711138229831eeda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# setCollectionViewLayout(_:animated:completion:)

<sub>Instance Method</sub>

Changes the collection view’s layout and notifies you when the animations complete.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated: Bool, completion: ((Bool) -> Void)? = nil)
```

## Parameters

- `layout` — The new layout object for the collection view.

- `animated` — Specify [true](../../swift/true.md) if you want to animate changes from the current layout to the new layout specified by the `layout` parameter. Specify [false](../../swift/false.md) to make the change without animations.

- `completion` — The block that’s executed when the layout transition finishes or is terminated by the user. This block takes the following parameter: - **finished** — A Boolean indicating whether the transition completed successfully. This parameter is [true](../../swift/true.md) if the transition finished and the new layout is installed. It’s [false](../../swift/false.md) if the user aborted the transition and returned to the old layout.

## Discussion

This method initiates a layout change programmatically, notifying you when the transition is complete. If you choose to animate the layout change, the animation timing and parameters are controlled by the collection view.

## See Also

### Changing the layout

- [collectionViewLayout](collectionviewlayout.md) — The layout used to organize the collected view’s items.
- [- setCollectionViewLayout:animated:](<setcollectionviewlayout(__animated_).md>) — Changes the collection view’s layout and optionally animates the change.
- [- startInteractiveTransitionToCollectionViewLayout:completion:](<startinteractivetransition(to_completion_).md>) — Changes the collection view’s current layout using an interactive transition effect.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Tells the collection view to finish an interactive transition by installing the intended target layout.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Tells the collection view to cancel an interactive transition and return to its original layout object.
- [LayoutInteractiveTransitionCompletion](layoutinteractivetransitioncompletion.md) — The completion block called at the end of an interactive transition for a collection view.
