---
title: allowsSelectionDuringEditing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/allowsselectionduringediting
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/allowsselectionduringediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/allowsselectionduringediting.json'
content_hash: 'sha256:e21526e7be6e9c6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# allowsSelectionDuringEditing

<sub>Instance Property</sub>

A Boolean value that determines whether users can select cells while the collection view is in editing mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsSelectionDuringEditing: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

## See Also

### Selecting cells

- [indexPathsForSelectedItems](indexpathsforselecteditems.md) — The index paths for the selected items.
- [- selectItemAtIndexPath:animated:scrollPosition:](<selectitem(at_animated_scrollposition_).md>) — Selects the item at the specified index path and optionally scrolls it into view.
- [- deselectItemAtIndexPath:animated:](<deselectitem(at_animated_).md>) — Deselects the item at the specified index.
- [allowsSelection](allowsselection.md) — A Boolean value that indicates whether users can select items in the collection view.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether users can select more than one item in the collection view.
- [allowsMultipleSelectionDuringEditing](allowsmultipleselectionduringediting.md) — A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
