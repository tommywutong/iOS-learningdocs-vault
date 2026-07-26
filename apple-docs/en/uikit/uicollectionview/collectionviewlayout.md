---
title: collectionViewLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/collectionviewlayout
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/collectionviewlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/collectionviewlayout.json'
content_hash: 'sha256:353c414cb5abbc94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# collectionViewLayout

<sub>Instance Property</sub>

The layout used to organize the collected view’s items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var collectionViewLayout: UICollectionViewLayout { get set }
```

## Discussion

Assigning a new layout object to this property causes the new layout to be applied (without animations) to the collection view’s items.

For more information, see [Layouts](../uicollectionview.md#Layouts).

## See Also

### Changing the layout

- [- setCollectionViewLayout:animated:](<setcollectionviewlayout(__animated_).md>) — Changes the collection view’s layout and optionally animates the change.
- [- setCollectionViewLayout:animated:completion:](<setcollectionviewlayout(__animated_completion_).md>) — Changes the collection view’s layout and notifies you when the animations complete.
- [- startInteractiveTransitionToCollectionViewLayout:completion:](<startinteractivetransition(to_completion_).md>) — Changes the collection view’s current layout using an interactive transition effect.
- [- finishInteractiveTransition](<finishinteractivetransition().md>) — Tells the collection view to finish an interactive transition by installing the intended target layout.
- [- cancelInteractiveTransition](<cancelinteractivetransition().md>) — Tells the collection view to cancel an interactive transition and return to its original layout object.
- [LayoutInteractiveTransitionCompletion](layoutinteractivetransitioncompletion.md) — The completion block called at the end of an interactive transition for a collection view.
