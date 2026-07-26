---
title: nextFocusedIndexPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewfocusupdatecontext/nextfocusedindexpath
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext/nextfocusedindexpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewfocusupdatecontext/nextfocusedindexpath.json'
content_hash: 'sha256:8af922be282b69b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFocusUpdateContext](../uicollectionviewfocusupdatecontext.md)

# nextFocusedIndexPath

<sub>Instance Property</sub>

The index path of the collection view cell that’s receiving the focus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var nextFocusedIndexPath: IndexPath? { get }
```

## Discussion

This property contains the index path only when the view receiving focus belongs to a cell of the collection view. If focus is moving to a view outside of the collection view and its cells, this property is `nil`.

## See Also

### Locating focusable items in the collection view

- [previouslyFocusedIndexPath](previouslyfocusedindexpath.md) — The index path of the collection view cell that previously had the focus.
