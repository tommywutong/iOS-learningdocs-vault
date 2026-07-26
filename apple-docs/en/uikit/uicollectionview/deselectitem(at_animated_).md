---
title: 'deselectItem(at:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/deselectitem(at:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/deselectitem(at:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/deselectitem%28at%3Aanimated%3A%29.json'
content_hash: 'sha256:666f19ff9a820920'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# deselectItem(at:animated:)

<sub>Instance Method</sub>

Deselects the item at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func deselectItem(at indexPath: IndexPath, animated: Bool)
```

## Parameters

- `indexPath` — The index path of the item to select. Specifying `nil` results in no change to the current selection.

- `animated` — Specify [true](../../swift/true.md) to animate the change in the selection or [false](../../swift/false.md) to make the change without animating it.

## Discussion

If the [allowsSelection](allowsselection.md) property is [false](../../swift/false.md), calling this method has no effect.

This method doesn’t cause any selection-related delegate methods to be called.

## See Also

### Selecting cells

- [indexPathsForSelectedItems](indexpathsforselecteditems.md) — The index paths for the selected items.
- [- selectItemAtIndexPath:animated:scrollPosition:](<selectitem(at_animated_scrollposition_).md>) — Selects the item at the specified index path and optionally scrolls it into view.
- [allowsSelection](allowsselection.md) — A Boolean value that indicates whether users can select items in the collection view.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether users can select more than one item in the collection view.
- [allowsSelectionDuringEditing](allowsselectionduringediting.md) — A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [allowsMultipleSelectionDuringEditing](allowsmultipleselectionduringediting.md) — A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
