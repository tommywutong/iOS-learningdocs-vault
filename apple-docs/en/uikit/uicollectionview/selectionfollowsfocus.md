---
title: selectionFollowsFocus
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/selectionfollowsfocus
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/selectionfollowsfocus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/selectionfollowsfocus.json'
content_hash: 'sha256:1b587b3e5c301812'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# selectionFollowsFocus

<sub>Instance Property</sub>

A Boolean value that triggers an automatic selection when focus moves to a cell.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var selectionFollowsFocus: Bool { get set }
```

## Discussion

The system determines the default value of this property according to the platform and other properties of the collection view.

## See Also

### Selecting cells

- [indexPathsForSelectedItems](indexpathsforselecteditems.md) — The index paths for the selected items.
- [- selectItemAtIndexPath:animated:scrollPosition:](<selectitem(at_animated_scrollposition_).md>) — Selects the item at the specified index path and optionally scrolls it into view.
- [- deselectItemAtIndexPath:animated:](<deselectitem(at_animated_).md>) — Deselects the item at the specified index.
- [allowsSelection](allowsselection.md) — A Boolean value that indicates whether users can select items in the collection view.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether users can select more than one item in the collection view.
- [allowsSelectionDuringEditing](allowsselectionduringediting.md) — A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [allowsMultipleSelectionDuringEditing](allowsmultipleselectionduringediting.md) — A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
