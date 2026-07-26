---
title: invalidateEverything
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateeverything
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateeverything'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateeverything.json'
content_hash: 'sha256:d9076a964190de79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# invalidateEverything

<sub>Instance Property</sub>

A Boolean that indicates that all layout data should be marked as invalid.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var invalidateEverything: Bool { get }
```

## Discussion

You do not set this property yourself. The collection view sets it in response to specific types of layout invalidation scenarios. For example, the collection view sets it to [true](../../swift/true.md) when you change the current layout object, change the data source of the collection view, or call the [- reloadData](<../uicollectionview/reloaddata().md>) method and subsequently request a layout invalidation context.

If this property is set to [true](../../swift/true.md), the layout object should recompute all of its layout-related data.

## See Also

### Invalidating the Collection View Data

- [invalidateDataSourceCounts](invalidatedatasourcecounts.md) — A Boolean that indicates whether the layout should ask for new section and item counts.
