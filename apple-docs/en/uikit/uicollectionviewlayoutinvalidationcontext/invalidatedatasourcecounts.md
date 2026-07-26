---
title: invalidateDataSourceCounts
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedatasourcecounts
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedatasourcecounts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedatasourcecounts.json'
content_hash: 'sha256:12fcb045a35a038c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# invalidateDataSourceCounts

<sub>Instance Property</sub>

A Boolean that indicates whether the layout should ask for new section and item counts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var invalidateDataSourceCounts: Bool { get }
```

## Discussion

You do not set this property yourself. The collection view sets it in response to specific types of layout invalidation scenarios.  For example, the collection view sets it to [true](../../swift/true.md) when you insert or delete items or call the collection view’s [- reloadData](<../uicollectionview/reloaddata().md>) method.

If this property is set to [true](../../swift/true.md), the layout object should query its delegate for the number of sections and items and update its layout based on the new number of items.

## See Also

### Invalidating the Collection View Data

- [invalidateEverything](invalidateeverything.md) — A Boolean that indicates that all layout data should be marked as invalid.
