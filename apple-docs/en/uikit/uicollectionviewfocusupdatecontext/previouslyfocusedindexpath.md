---
title: previouslyFocusedIndexPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewfocusupdatecontext/previouslyfocusedindexpath
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext/previouslyfocusedindexpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewfocusupdatecontext/previouslyfocusedindexpath.json'
content_hash: 'sha256:585375805e811285'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFocusUpdateContext](../uicollectionviewfocusupdatecontext.md)

# previouslyFocusedIndexPath

<sub>Instance Property</sub>

The index path of the collection view cell that previously had the focus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var previouslyFocusedIndexPath: IndexPath? { get }
```

## Discussion

This property contains an index path only when the view receiving focus belongs to a cell of the collection view. If focus was previously in a view outside of the collection view and its cells, this property is `nil`. This property is also `nil` when the collection view receives focus for the first time.

## See Also

### Locating focusable items in the collection view

- [nextFocusedIndexPath](nextfocusedindexpath.md) — The index path of the collection view cell that’s receiving the focus.
