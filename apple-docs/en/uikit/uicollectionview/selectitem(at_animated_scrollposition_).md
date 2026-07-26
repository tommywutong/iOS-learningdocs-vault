---
title: 'selectItem(at:animated:scrollPosition:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/selectitem(at:animated:scrollposition:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/selectitem(at:animated:scrollposition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/selectitem%28at%3Aanimated%3Ascrollposition%3A%29.json'
content_hash: 'sha256:fac5707a186cb285'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# selectItem(at:animated:scrollPosition:)

<sub>Instance Method</sub>

Selects the item at the specified index path and optionally scrolls it into view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func selectItem(at indexPath: IndexPath?, animated: Bool, scrollPosition: UICollectionView.ScrollPosition)
```

## Parameters

- `indexPath` — The index path of the item to select. Specifying `nil` for this parameter clears the current selection.

- `animated` — Specify [true](../../swift/true.md) to animate the change in the selection or [false](../../swift/false.md) to make the change without animating it.

- `scrollPosition` — An option that specifies where the item should be positioned when scrolling finishes. For a list of possible values, see [ScrollPosition](scrollposition.md).

## Discussion

If the [allowsSelection](allowsselection.md) property is [false](../../swift/false.md), calling this method has no effect. If there’s an existing selection with a different index path and the [allowsMultipleSelection](allowsmultipleselection.md) property is [false](../../swift/false.md), calling this method replaces the previous selection.

This method doesn’t cause any selection-related delegate methods to be called.

## See Also

### Selecting cells

- [indexPathsForSelectedItems](indexpathsforselecteditems.md) — The index paths for the selected items.
- [- deselectItemAtIndexPath:animated:](<deselectitem(at_animated_).md>) — Deselects the item at the specified index.
- [allowsSelection](allowsselection.md) — A Boolean value that indicates whether users can select items in the collection view.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether users can select more than one item in the collection view.
- [allowsSelectionDuringEditing](allowsselectionduringediting.md) — A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [allowsMultipleSelectionDuringEditing](allowsmultipleselectionduringediting.md) — A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
