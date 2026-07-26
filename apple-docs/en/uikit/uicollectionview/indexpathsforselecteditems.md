---
title: indexPathsForSelectedItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/indexpathsforselecteditems
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/indexpathsforselecteditems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/indexpathsforselecteditems.json'
content_hash: 'sha256:f9b059e2627d1206'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# indexPathsForSelectedItems

<sub>Instance Property</sub>

The index paths for the selected items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indexPathsForSelectedItems: [IndexPath]? { get }
```

## Discussion

The value of this property is an array of [NSIndexPath](../../foundation/nsindexpath.md) objects, each of which corresponds to a single selected item. If there are no selected items, the value of this property is `nil`.

## See Also

### Selecting cells

- [- selectItemAtIndexPath:animated:scrollPosition:](<selectitem(at_animated_scrollposition_).md>) — Selects the item at the specified index path and optionally scrolls it into view.
- [- deselectItemAtIndexPath:animated:](<deselectitem(at_animated_).md>) — Deselects the item at the specified index.
- [allowsSelection](allowsselection.md) — A Boolean value that indicates whether users can select items in the collection view.
- [allowsMultipleSelection](allowsmultipleselection.md) — A Boolean value that determines whether users can select more than one item in the collection view.
- [allowsSelectionDuringEditing](allowsselectionduringediting.md) — A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [allowsMultipleSelectionDuringEditing](allowsmultipleselectionduringediting.md) — A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
