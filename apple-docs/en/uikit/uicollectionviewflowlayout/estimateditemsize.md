---
title: estimatedItemSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/estimateditemsize
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/estimateditemsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/estimateditemsize.json'
content_hash: 'sha256:f99a3d0e3223a993'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# estimatedItemSize

<sub>Instance Property</sub>

The estimated size of cells in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var estimatedItemSize: CGSize { get set }
```

## Discussion

Providing an estimated cell size can improve the performance of the collection view when the cells adjust their size dynamically. The estimated value lets the collection view defer some calculations to determine the actual size of its content. Cells that aren’t onscreen are assumed to be the estimated height.

The default value of this property is [CGSizeZero](../../coregraphics/cgsizezero.md). Setting it to any other value, like [UICollectionViewFlowLayoutAutomaticSize](automaticsize.md), causes the collection view to query each cell for its actual size using the cell’s [- preferredLayoutAttributesFittingAttributes:](<../uicollectionreusableview/preferredlayoutattributesfitting(__).md>) method.

If all of your cells are the same size, use the [itemSize](itemsize.md) property, instead of this property, to specify the cell size instead.

## See Also

### Configuring item spacing

- [minimumLineSpacing](minimumlinespacing.md) — The minimum spacing to use between lines of items in the grid.
- [minimumInteritemSpacing](minimuminteritemspacing.md) — The minimum spacing to use between items in the same row.
- [itemSize](itemsize.md) — The default size to use for cells.
- [UICollectionViewFlowLayoutAutomaticSize](automaticsize.md) — A placeholder size for self-sizing cells.
- [sectionInset](sectioninset.md) — The margins used to lay out content in a section.
- [sectionInsetReference](sectioninsetreference-swift.property.md) — The boundary that section insets are defined in relation to.
- [SectionInsetReference](sectioninsetreference-swift.enum.md) — Constants that describe the reference point of the section insets.
