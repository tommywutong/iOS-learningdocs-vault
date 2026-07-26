---
title: UICollectionView.LayoutInteractiveTransitionCompletion
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/layoutinteractivetransitioncompletion
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/layoutinteractivetransitioncompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/layoutinteractivetransitioncompletion.json'
content_hash: 'sha256:8d8bb50a7b47a36f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# UICollectionView.LayoutInteractiveTransitionCompletion

<sub>Type Alias</sub>

The completion block called at the end of an interactive transition for a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias LayoutInteractiveTransitionCompletion = (Bool, Bool) -> Void
```

## Discussion

This completion block takes the following parameters:

- **completed** — A Boolean indicating whether the animations ran to completion.
- **finish** — A Boolean indicating whether the transition finished or was canceled. This parameter is [true](../../swift/true.md) if the transition ran to completion and the new layout is installed. It is [false](../../swift/false.md) if the user canceled the transition and the old layout is installed.

## See Also

### Changing the layout

- [collectionViewLayout](collectionviewlayout.md) — The layout used to organize the collected view’s items.
- [- setCollectionViewLayout:animated:](<setcollectionviewlayout(__animated_).md>) — Changes the collection view’s layout and optionally animates the change.
- [- setCollectionViewLayout:animated:completion:](<setcollectionviewlayout(__animated_completion_).md>) — Changes the collection view’s layout and notifies you when the animations complete.
- [- startInteractiveTransitionToCollectionViewLayout:completion:](<startinteractivetransition(to_completion_).md>) — Changes the collection view’s current layout using an interactive transition effect.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Tells the collection view to finish an interactive transition by installing the intended target layout.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Tells the collection view to cancel an interactive transition and return to its original layout object.
