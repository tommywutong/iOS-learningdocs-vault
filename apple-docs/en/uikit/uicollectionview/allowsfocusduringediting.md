---
title: allowsFocusDuringEditing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/allowsfocusduringediting
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/allowsfocusduringediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/allowsfocusduringediting.json'
content_hash: 'sha256:7df153bd344fd956'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# allowsFocusDuringEditing

<sub>Instance Property</sub>

A Boolean value that determines whether the collection view allows its cells to become focused in edit mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsFocusDuringEditing: Bool { get set }
```

## Discussion

If you implement [- collectionView:canFocusItemAtIndexPath:](<../uicollectionviewdelegate/collectionview(__canfocusitemat_).md>), its return value takes precedence over the value of this property.

The system determines the default value of this property according to the platform and other properties of the collection view.

## See Also

### Working with focus

- [allowsFocus](allowsfocus.md) — A Boolean value that determines whether the collection view allows its cells to become focused.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
- [remembersLastFocusedIndexPath](rememberslastfocusedindexpath.md) — A Boolean value that indicates whether the collection view automatically assigns the focus to the item at the last focused index path.
