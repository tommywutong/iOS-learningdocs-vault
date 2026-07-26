---
title: itemSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/itemsize
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/itemsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/itemsize.json'
content_hash: 'sha256:f19ba0b3857dc894'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# itemSize

<sub>Instance Property</sub>

The default size to use for cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var itemSize: CGSize { get set }
```

## Discussion

If the delegate does not implement the [- collectionView:layout:sizeForItemAtIndexPath:](<../uicollectionviewdelegateflowlayout/collectionview(__layout_sizeforitemat_).md>) method, the flow layout uses the value in this property to set the size of each cell. This results in cells that all have the same size.

The default size value is (50.0, 50.0).

## See Also

### Configuring item spacing

- [minimumLineSpacing](minimumlinespacing.md) — The minimum spacing to use between lines of items in the grid.
- [minimumInteritemSpacing](minimuminteritemspacing.md) — The minimum spacing to use between items in the same row.
- [estimatedItemSize](estimateditemsize.md) — The estimated size of cells in the collection view.
- [UICollectionViewFlowLayoutAutomaticSize](automaticsize.md) — A placeholder size for self-sizing cells.
- [sectionInset](sectioninset.md) — The margins used to lay out content in a section.
- [sectionInsetReference](sectioninsetreference-swift.property.md) — The boundary that section insets are defined in relation to.
- [SectionInsetReference](sectioninsetreference-swift.enum.md) — Constants that describe the reference point of the section insets.
