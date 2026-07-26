---
title: 'setCollectionViewLayout(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/setcollectionviewlayout(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/setcollectionviewlayout(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/setcollectionviewlayout%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:11c8df13d7fb417e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# setCollectionViewLayout(_:animated:)

<sub>Instance Method</sub>

Changes the collection view’s layout and optionally animates the change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated: Bool)
```

## Parameters

- `layout` — The new layout object for the collection view.

- `animated` — Specify [true](../../swift/true.md) if you want to animate changes from the current layout to the new layout specified by the `layout` parameter. Specify [false](../../swift/false.md) to make the change without animations.

## Discussion

This method makes the layout change without further interaction from the user. If you choose to animate the layout change, the animation timing and parameters are controlled by the collection view.

## See Also

### Changing the layout

- [collectionViewLayout](collectionviewlayout.md) — The layout used to organize the collected view’s items.
- [- setCollectionViewLayout:animated:completion:](<setcollectionviewlayout(__animated_completion_).md>) — Changes the collection view’s layout and notifies you when the animations complete.
- [- startInteractiveTransitionToCollectionViewLayout:completion:](<startinteractivetransition(to_completion_).md>) — Changes the collection view’s current layout using an interactive transition effect.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Tells the collection view to finish an interactive transition by installing the intended target layout.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Tells the collection view to cancel an interactive transition and return to its original layout object.
- [LayoutInteractiveTransitionCompletion](layoutinteractivetransitioncompletion.md) — The completion block called at the end of an interactive transition for a collection view.
