---
title: allowsMultipleSelection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/allowsmultipleselection
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/allowsmultipleselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/allowsmultipleselection.json'
content_hash: 'sha256:6aa084e051ea9359'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# allowsMultipleSelection

<sub>Instance Property</sub>

A Boolean value that determines whether users can select more than one item in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsMultipleSelection: Bool { get set }
```

## Discussion

This property controls whether multiple items can be selected simultaneously. The default value of this property is [false](../../swift/false.md).

When the value of this property is [true](../../swift/true.md), tapping a cell adds it to the current selection (assuming the delegate permits the cell to be selected). Tapping the cell again removes it from the selection.

## See Also

### Selecting cells

- [indexPathsForSelectedItems](indexpathsforselecteditems.md) — The index paths for the selected items.
- [- selectItemAtIndexPath:animated:scrollPosition:](<selectitem(at_animated_scrollposition_).md>) — Selects the item at the specified index path and optionally scrolls it into view.
- [- deselectItemAtIndexPath:animated:](<deselectitem(at_animated_).md>) — Deselects the item at the specified index.
- [allowsSelection](allowsselection.md) — A Boolean value that indicates whether users can select items in the collection view.
- [allowsSelectionDuringEditing](allowsselectionduringediting.md) — A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [allowsMultipleSelectionDuringEditing](allowsmultipleselectionduringediting.md) — A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
