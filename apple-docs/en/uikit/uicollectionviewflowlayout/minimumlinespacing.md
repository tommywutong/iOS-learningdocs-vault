---
title: minimumLineSpacing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/minimumlinespacing
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/minimumlinespacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/minimumlinespacing.json'
content_hash: 'sha256:ced9355088db20ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# minimumLineSpacing

<sub>Instance Property</sub>

The minimum spacing to use between lines of items in the grid.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimumLineSpacing: CGFloat { get set }
```

## Discussion

If the delegate object does not implement the [- collectionView:layout:minimumLineSpacingForSectionAtIndex:](<../uicollectionviewdelegateflowlayout/collectionview(__layout_minimumlinespacingforsectionat_).md>) method, the flow layout uses the value in this property to set the spacing between lines in a section.

For a vertically scrolling grid, this value represents the minimum spacing between successive rows. For a horizontally scrolling grid, this value represents the minimum spacing between successive columns. This spacing is not applied to the space between the header and the first line or between the last line and the footer.

The default value of this property is 10.0.

## See Also

### Configuring item spacing

- [minimumInteritemSpacing](minimuminteritemspacing.md) — The minimum spacing to use between items in the same row.
- [itemSize](itemsize.md) — The default size to use for cells.
- [estimatedItemSize](estimateditemsize.md) — The estimated size of cells in the collection view.
- [UICollectionViewFlowLayoutAutomaticSize](automaticsize.md) — A placeholder size for self-sizing cells.
- [sectionInset](sectioninset.md) — The margins used to lay out content in a section.
- [sectionInsetReference](sectioninsetreference-swift.property.md) — The boundary that section insets are defined in relation to.
- [SectionInsetReference](sectioninsetreference-swift.enum.md) — Constants that describe the reference point of the section insets.
