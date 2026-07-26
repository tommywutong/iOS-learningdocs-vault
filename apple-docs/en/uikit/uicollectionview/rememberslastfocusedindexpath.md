---
title: remembersLastFocusedIndexPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/rememberslastfocusedindexpath
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/rememberslastfocusedindexpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/rememberslastfocusedindexpath.json'
content_hash: 'sha256:f4cba0d4e7614310'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# remembersLastFocusedIndexPath

<sub>Instance Property</sub>

A Boolean value that indicates whether the collection view automatically assigns the focus to the item at the last focused index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var remembersLastFocusedIndexPath: Bool { get set }
```

## Discussion

When this property is set to [true](../../swift/true.md), the collection view remembers which index path was focused when focus leaves the collection view. When it receives the focus again, the collection view automatically redirects that focus back to the previously focused index path. The default value of this property is [false](../../swift/false.md).

The effects of this property may be ignored during or immediately after a view controller transition, such as a presentation dismissal or navigation stack pop. In such cases, the view controller attempts to restore focus to the item that was focused prior to the transition (for example, prior to the view controller being presented or pushed), which can take precedence over the effects of this property. To learn how to control or disable this behavior in the view controller, see [restoresFocusAfterTransition](../uiviewcontroller/restoresfocusaftertransition.md).

## See Also

### Working with focus

- [allowsFocus](allowsfocus.md) — A Boolean value that determines whether the collection view allows its cells to become focused.
- [allowsFocusDuringEditing](allowsfocusduringediting.md) — A Boolean value that determines whether the collection view allows its cells to become focused in edit mode.
- [selectionFollowsFocus](selectionfollowsfocus.md) — A Boolean value that triggers an automatic selection when focus moves to a cell.
